An independently maintained fork of [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi).

This release distributes the maintainer's existing, working macOS application: version **0.8.3**, build **20260929.091845**, for **Apple Silicon (arm64)**.

Download the ZIP and extract `OpenLogi.app`. It includes the desktop GUI, agent, overlay, and CLI. This is the exact installed application snapshot, preserved without rebuilding or changing its bundle. It is signed with a local code-signing certificate and is not an official upstream release. Another Mac may require Accessibility and Input Monitoring permissions.

The archived application predates the repository's current source snapshot and retains its original branding. OpenLogi source code is dual-licensed MIT/Apache-2.0; upstream brand assets retain their separate proprietary license.

Validation: all extracted files and executable permissions match the installed application; macOS signature verification passed. The publishing workflow also verifies ZIP integrity, version, build number, and the presence of all four executables.
