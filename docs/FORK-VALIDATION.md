# Source publication validation

The publication preserves the local source snapshot rather than rebasing onto a
new upstream version. The inherited source version is 0.8.3. This is a source
publication, not an installer Release or a crates.io publication.

## Local checks

On macOS arm64 with Rust 1.98, with `RUSTFLAGS=-D warnings` and Xcode 26 selected:

- `cargo fmt --all -- --check`
- `cargo clippy --workspace --all-targets -- -D warnings`
- `cargo test --workspace --all-targets` — 1,382 passed, zero failures or ignored tests.
- `RUSTDOCFLAGS="-D warnings" cargo doc --workspace --no-deps --document-private-items --exclude openlogi-ui --exclude openlogi-desktop --exclude openlogi-overlay --exclude openlogi-agent`
- `cargo check -p openlogi-device-registry -p openlogi-hidpp -p openlogi-device --target wasm32-unknown-unknown` — portable crates passed.
- `cargo check -p openlogi-core --no-default-features --target wasm32-unknown-unknown` — portable core passed.
- `cargo deny --config .cargo/deny.toml --all-features --manifest-path crates/openlogi/Cargo.toml check` — dependency audit passed.
- `cargo xtask ci clippy-windows` — the repository's ring-free Windows proxy passed; this is not the full native Windows job.
- `cargo clippy --target aarch64-unknown-linux-musl -p openlogi-hook -p openlogi-inject -p openlogi-hid -p openlogi-hidpp -p openlogi-core -p openlogi-agent -p openlogi-agent-core -p openlogi-ipc -p openlogi-permissions --all-targets -- -D warnings` — the supported Linux cross-lint subset passed.
- `cargo xtask ci publish-closure` — all 13 publishable workspace packages have a valid dependency closure.
- `OPENLOGI_DEVELOPER_DIR=/Applications/Xcode-26.0.1.app/Contents/Developer cargo xtask macos icon` — both original fork icon documents compile.
- `OPENLOGI_DIALOG_SMOKE=1 target/debug/openlogi-desktop` — native hidden-window rendering, rename input focus/typing, and delete dialog checks passed without opening a visible window.
- `actionlint -shellcheck= -pyflakes= .github/workflows/release-plz.yml .github/workflows/release.yml` — modified workflow definitions passed.
- `typos --config .config/typos.toml --force-exclude .`
- `git diff --check`

The final unsigned development bundle is validated with
`OPENLOGI_LOCAL_CODESIGN=0 OPENLOGI_DEVELOPER_DIR=/Applications/Xcode-26.0.1.app/Contents/Developer cargo xtask macos bundle --channel dev`.
No installer is uploaded. No release tag is created.

## Limits and hardware verification

Not runtime-tested on hardware in this publication task. The full native Linux
and Windows jobs, and macOS x86_64, require the GitHub CI matrix; the local proxies
cannot establish those results. There was no interactive visual review of the
full application. Upstream updater, config paths, binary names and production
bundle identities remain inherited; independent binary distribution needs its
own product identity, signing and update channel first.

To verify on hardware, build the development channel, grant Input Monitoring
and Accessibility to its bundled agent, connect a supported Logitech device,
and exercise remapped buttons across display sleep and session lock/unlock.
Check that input remains pass-through while inactive and recovers on return.
Verify the device menu's Rename/Delete actions by mouse and keyboard. Switch
both Dock icon choices and confirm the application bundle signature stays valid.
