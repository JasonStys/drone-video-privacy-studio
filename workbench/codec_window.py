"""Jason Stys: explicit dependency consent before profiles, cancel and visible bounded setup outcomes. Lines: docs/SOURCE_MAP.md."""

import queue
import threading
import tkinter as tk
from tkinter import ttk

from workbench import codec_setup

TERMS = (
    "The application download does not contain PyAV or FFmpeg codecs. Install the exact official PyPI wheel below to enable local video processing. "
    "PyAV's binding uses BSD terms; its bundled FFmpeg/codecs retain separate upstream GPL/LGPL, copyright and possible patent obligations. "
    "This download design does not certify those terms or grant codec-patent clearance. Upstream notices remain in the installed wheel. "
    "The provider receives a normal HTTPS dependency request (including connection metadata); no footage, account information or profile files are sent. "
    "Setup contacts only the displayed pinned files.pythonhosted.org URL, verifies its length/SHA256/ABI and safely installs it without pip or source builds. "
    "Later launches verify and use it offline. Cancel leaves accounts and footage unopened."
)


class DependencyWindow:
    """A real native install/cancel choice; an in-progress bounded download is joined before the window closes."""

    def __init__(self, root, home, pin):
        """Show exact provider/version/size/terms before permitting network access or profile setup."""
        self.root, self.home, self.pin = root, home, pin
        self.accepted, self.thread = False, None
        self.events = queue.Queue()
        root.title("Drone Video Privacy Studio — video dependency setup")
        root.geometry("780x640")
        root.minsize(700, 600)
        root.protocol("WM_DELETE_WINDOW", self.cancel)
        shell = ttk.Frame(root, padding=22)
        shell.pack(fill="both", expand=True)
        actions = ttk.Frame(shell)
        actions.pack(fill="x", side="bottom", pady=(14, 0))
        self.install_button = ttk.Button(
            actions, text="Install verified video dependency", command=self.install
        )
        self.install_button.pack(side="left")
        self.cancel_button = ttk.Button(
            actions, text="Cancel without opening data", command=self.cancel
        )
        self.cancel_button.pack(side="right")
        ttk.Label(
            shell, text="Enable private local video processing", font=("TkDefaultFont", 17, "bold")
        ).pack(anchor="w")
        ttk.Label(shell, text="Jason Stys · optional first-run dependency download").pack(
            anchor="w", pady=(6, 12)
        )
        self.text = tk.Text(shell, wrap="word", height=12, padx=10, pady=10)
        scrollbar = ttk.Scrollbar(shell, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.text.pack(fill="both", expand=True)
        self.text.insert("1.0", TERMS + "\n\n" + description(pin))
        self.text.configure(state="disabled")
        self.status = tk.StringVar(
            value="No network request has been made. Choose Install or Cancel."
        )
        ttk.Label(shell, textvariable=self.status, wraplength=640).pack(anchor="w", pady=(12, 0))

    def install(self):
        """Only this explicit button starts a single owned installer thread, never a profile or server."""
        if self.thread is not None:
            return
        self.install_button.configure(state="disabled")
        self.cancel_button.configure(state="disabled")
        self.status.set(
            "Downloading and verifying the displayed wheel. Wait for completion; no accounts or footage are open."
        )

        def run():
            """Return a safe ordinary error; the non-daemon thread retains ownership until its bounded operation ends."""
            try:
                codec_setup.install(self.home, self.pin)
                self.events.put(None)
            except Exception as error:
                self.events.put(str(error))

        self.thread = threading.Thread(target=run, name="explicit-codec-install")
        self.thread.start()
        self.root.after(40, self.poll)

    def poll(self):
        """Observe completion without a retrying network request or fixed success sleep."""
        if self.thread.is_alive():
            self.root.after(40, self.poll)
            return
        self.thread.join()
        error = self.events.get_nowait()
        if error is None:
            self.accepted = True
            self.root.destroy()
        else:
            self.status.set(
                "Setup failed; existing data were not replaced. "
                + error
                + " Quit and reopen after correcting the cause."
            )
            self.cancel_button.configure(state="normal")

    def cancel(self):
        """Before install, Cancel performs no fetch; during install retain ownership instead of abandoning a writer."""
        if self.thread is not None and self.thread.is_alive():
            self.status.set(
                "Setup is still completing. Wait for its bounded operation, then close this window."
            )
            return
        self.root.destroy()


def description(pin):
    """Public immutable identity displayed in both native GUI and optional explicit console consent."""
    return (
        f"Provider: official PyPI / files.pythonhosted.org\nDependency: PyAV {codec_setup.VERSION}\n"
        f"File: {pin['filename']}\nBytes: {pin['bytes']:,}\nSHA256: {pin['sha256']}\nABI: {pin['tag']}\n"
        f"Exact URL: {pin['url']}\nUpstream terms/source: https://github.com/PyAV-Org/PyAV/tree/a4ad0133b13eb84067dc6e8105eb1fc8f8b93c4f"
    )


def ensure(*, interactive=True, console=False):
    """Require prior offline verification; only an explicit normal GUI/console choice can install an absent wheel."""
    pin, home = codec_setup.selected_pin(), codec_setup.dependency_home()
    if not codec_setup.has_installation(home, pin):
        if console:
            print(TERMS + "\n\n" + description(pin), flush=True)
            if (
                input(
                    "Type INSTALL to download this exact dependency, or anything else to cancel: "
                )
                != "INSTALL"
            ):
                return False
            codec_setup.install(home, pin)
        elif interactive:
            root = tk.Tk()
            window = DependencyWindow(root, home, pin)
            root.mainloop()
            if not window.accepted:
                return False
        else:
            raise ValueError(
                "Video dependency is absent; open normal setup or explicitly use --install-codecs first"
            )
    codec_setup.activate(home, pin)
    return True
