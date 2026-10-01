# LogiLocal — an independent OpenLogi fork

![LogiLocal icon](design/icon/openlogi-128.png)

This repository is [komakizhu's maintained fork](https://github.com/komakizhu/OpenLogi)
of [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi). It is not an official
OpenLogi release and is not affiliated with the upstream maintainers or Logitech.
The original Git history, authorship, MIT/Apache-2.0 licenses, and 0BSD notices are preserved.

This source publication includes our local macOS session/input-hook recovery fixes,
agent-launch recovery, device-menu and dialog fixes, and a Dock icon picker that
keeps signed bundles intact. It retains upstream functionality and technical
identifiers for compatibility. No fork installer or binary release is published yet. Upstream release workflows
are restricted to the upstream repository; this fork keeps CI enabled.
Use the development channel when building locally; production bundle identities
and the upstream updater have not been migrated to an independent release channel.
Do not configure an upstream update signing key for fork builds.

The artwork in the current tree is original LogiLocal artwork, licensed under MIT.
Historical OpenLogi brand assets remain proprietary to their original owners;
their presence in inherited Git history grants no permission to reuse them.

Build instructions: [developer handbook](docs/DEVELOPMENT.md).
[Publication validation and hardware test instructions](docs/FORK-VALIDATION.md).
[中文 fork 说明](docs/FORK.zh-CN.md). The feature documentation below describes the
inherited OpenLogi implementation; upstream downloads are upstream builds.

## Beyond Options+

Things OpenLogi does that Options+ won't:

- **Stay light.** Native Rust + GPUI.
- **Run on Linux.** Linux is a first-class platform in OpenLogi.
- **Gestures on any button.** Give the gesture role to any physical button — or turn gestures off entirely.
- **Plain-text config.** Everything is one TOML file you can sync between machines however you like.
- **Script it.** A real CLI alongside the GUI.

## Features

- Devices connected over Logi Bolt receivers, Unifying receivers, Bluetooth, or a wired connection, with battery percentage and charge state
- Button remapping via the OS input hook: a built-in action catalog plus custom keyboard shortcuts authored in the TOML config, including independent short/long-press actions and hold-until-release chords for push-to-talk¹
- Per-application profile overlays that auto-switch on app focus (macOS + Windows; Linux on X11 / XWayland only)
- Litra lights: power, brightness, and color temperature, with optional auto power that follows camera activity

**Mouse**

- Capture and remap the middle, mode-shift, and thumbwheel buttons (middle everywhere, the rest where the device exposes them)
- Per-direction gesture bindings with live capture, on any capable button
- Actions Ring: a cursor-centred, eight-slot overlay of actions (`ShowActionsRing`), with per-application layouts
- DPI control with presets and Cycle / Set-preset actions (`0x2201`)
- SmartShift wheel: mode toggle, sensitivity, and a permanent-ratchet panel (`0x2111`)
- Per-device native scroll inversion (`0x2121`, supported devices)

**Keyboard**

- Global F-key remapping: the same action catalog as the mouse, plus power-user actions — typed text, key combos, multi-step workflows (macOS + Windows)
- Static RGB lighting (`0x8070` / `0x8080`, supported devices)

**Camera**

- Any Logitech UVC webcam (Brio, StreamCam, the C920 series, …), plug and play
- Live preview that opens the camera only while you watch — leaving it releases the camera entirely and the LED goes off
- Image controls written straight to the UVC hardware — zoom, focus, exposure, brightness, contrast, saturation, sharpness, white balance, tint, anti-flicker, and low-light compensation, with auto-mode toggles for focus / exposure / white balance — so changes apply in Meet / Zoom / OBS and every other app using the camera
- One-click profiles: built-in Default / Streaming / Video call plus custom snapshots; settings persist per camera and are written back to the hardware on the next view

¹ Media key actions use D-Bus MPRIS on Linux; a handful of macOS-specific actions have no universal Linux equivalent and are no-ops. Windows maps platform actions to native equivalents where available.

## Install

> [!IMPORTANT]
> Quit **Logi Options+** first: the two applications fight over HID++ access, and only one can own a given receiver at a time.

### macOS

Requires macOS 13 or later.

Download the signed, notarized `.dmg` from the [latest release](https://github.com/AprilNEA/OpenLogi/releases/latest) and drag `OpenLogi.app` to `/Applications`.

Or install via [Homebrew](https://brew.sh):

```sh
brew install --cask openlogi
```

The official Homebrew cask is the default installation path. To explicitly
track the latest GitHub release from `aprilnea/tap` instead:

```sh
brew tap aprilnea/tap
brew install --cask aprilnea/tap/openlogi@latest
```

`openlogi@latest` is maintained by OpenLogi's release workflow and may update
before the official cask autobump lands. Install either `openlogi` or
`openlogi@latest`, not both.

### Linux

Download the package for your distribution from the
[latest release](https://github.com/AprilNEA/OpenLogi/releases/latest):

```sh
# Debian / Ubuntu
sudo dpkg -i openlogi_*.deb

# Fedora / RHEL
sudo rpm -i openlogi-*.rpm

# Arch Linux
sudo pacman -U openlogi-*.pkg.tar.zst
```

Packages are published for both `x86_64`/`amd64` and `arm64`/`aarch64`.
Pre-built packages require GLIBC 2.35 or newer (Ubuntu 22.04 baseline).

NixOS users can instead import the repository's module, which installs the
package and udev rules and starts the agent with the graphical session:

```nix
{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  inputs.openlogi = {
    url = "github:AprilNEA/OpenLogi";
    inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { nixpkgs, openlogi, ... }: {
    nixosConfigurations.my-host = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux"; # or aarch64-linux
      modules = [
        openlogi.nixosModules.default
        { programs.openlogi.enable = true; }
      ];
    };
  };
}
```

All Linux packages install udev rules that grant your user access to
`/dev/hidraw*`, `/dev/uinput` and your Logitech mouse's `/dev/input/event*`
node without `sudo`. The NixOS module starts the agent automatically; after a
`.deb`, `.rpm`, or `.pkg.tar.zst` installation, enable it for your user:

```sh
systemctl --user enable --now openlogi-agent.service
```

See [docs/INSTALL-linux.md](docs/INSTALL-linux.md) for complete NixOS options,
manual / source installs, and distros without systemd.

### Windows

Signed portable `.zip` archives and per-user `.msi` installers (x86_64 and
arm64) are attached to each release. Both ship the GUI (`OpenLogi.exe`)
together with the background agent (`openlogi-agent.exe`), which owns all
device I/O. Keep the two files side by side when using the portable zip, or
the GUI has nothing to connect to.

Windows support has been validated end-to-end on Windows 11 with real
hardware (a wired keyboard and a Unifying-receiver mouse), including
install, in-place upgrade, and uninstall of the MSI. It is newer than the
macOS build, so if you hit a rough edge please
[report it](https://github.com/AprilNEA/OpenLogi/issues). The agent shows a
system-tray icon (Show Main Window / Quit) so the app stays reachable after
the main window is closed. To disable it on Windows, set
`show_in_menu_bar = false` in the TOML `[app_settings]` block and restart the
agent; the GUI toggle is currently macOS-only.

To build from source, see [DEVELOPMENT.md](docs/DEVELOPMENT.md).


## Usage (CLI)

See [USAGE.md](docs/USAGE.md)

## Configuration

See [CONFIGURATION.md](docs/CONFIGURATION.md)

## Developing

See [DEVELOPMENT.md](docs/DEVELOPMENT.md)

## Acknowledgments

- **Windows, cameras, and i18n** by [@davidbudnick](https://github.com/davidbudnick) — keyboard RGB, Windows support, Logitech webcam support
- **Linux port** by [@cserby](https://github.com/cserby) — Linux support
- [Solaar](https://github.com/pwr-Solaar/Solaar) by [@pwr](https://github.com/pwr) — open-source HID++ implementation
- [Mouser](https://github.com/TomBadash/Mouser) by [@TomBadash](https://github.com/TomBadash) — a local, account-free Options+ replacement

## License

The code in this repository is dual-licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE))
- MIT license ([LICENSE-MIT](LICENSE-MIT))

at your option.

### Third-party code

`crates/openlogi-hidpp` is a vendored fork of [`hidpp`](https://crates.io/crates/hidpp)
by [@lus](https://github.com/lus), licensed 0BSD.

### Fork artwork

Current `design/` artwork and the bundled app icon are original LogiLocal assets
by komakizhu, licensed under MIT; see [design/LICENSE](design/LICENSE).
They were generated independently with [tools/generate-fork-art.py](tools/generate-fork-art.py).
Upstream OpenLogi names and branding belong to their respective owners; the
upstream artwork in inherited history retains its original proprietary license.

---

**Not affiliated with Logitech.** "Logitech", "MX Master", and "Options+" are trademarks of Logitech International S.A.
