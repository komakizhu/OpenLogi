# LogiLocal：独立维护的 OpenLogi fork

仓库：[komakizhu/OpenLogi](https://github.com/komakizhu/OpenLogi)。
上游：[AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)。
本仓库不是官方发行版，与上游维护者及 Logitech 无隶属关系。

这次发布的是本地源码，包含 macOS 会话切换后的输入钩子恢复、agent 启动与恢复、
设备菜单及对话框修复，以及不修改已签名应用包的 Dock 图标切换。
保留完整提交历史、作者信息、MIT／Apache-2.0 许可证和 HID++ 的 0BSD 声明。

当前图标及安装背景为原创 LogiLocal 素材，按 MIT 授权。
Git 历史中的上游品牌资产仍遵循原专有许可证，不能据此用于自己的发行版。

本次没有发布安装包。依赖上游凭据的自动发布流程仅允许在上游仓库运行，fork 保留 CI。源码中的程序名、配置路径、IPC、bundle 标识及 updater
仍沿用上游实现；本地编译请使用 dev 通道，避免作为独立生产发行版分发。
独立安装包发布前，需要迁移产品标识、签名和更新通道，不能使用上游更新签名密钥。
构建方法见 [开发手册](DEVELOPMENT.md)。
