# Local macOS application snapshot

[Download OpenLogi 0.8.3 for Apple Silicon Mac](./OpenLogi-macOS-arm64-0.8.3-20260929.091845.zip)

This archive contains the existing, locally modified application installed on the maintainer's Mac. It was copied directly from `/Applications/OpenLogi.app` without recompiling or changing the application bundle.

- Application version: `0.8.3`
- Build: `20260929.091845`
- Architecture: macOS arm64 (Apple Silicon)
- Bundle identifier: `org.openlogi.openlogi`
- Signing: local code-signing certificate; not an official upstream release

Extract the ZIP to obtain `OpenLogi.app`. The archive includes the GUI, agent, overlay, and CLI. Existing Accessibility and Input Monitoring permissions may need to be granted on another Mac.

This is an independently maintained fork of [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi). The archived application predates the current source snapshot and retains its original branding. OpenLogi source code is dual-licensed MIT/Apache-2.0; upstream brand assets retain their separate proprietary license.

Verification: the extracted application's files and executable permissions match the installed application exactly, and macOS code-signature verification passes. The application was not launched during packaging.
