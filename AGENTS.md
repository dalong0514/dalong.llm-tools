# 仓库指南

本仓库包含一组基于 Python 3.10+ 的工具工作台，用于 LLM 驱动的媒体处理、提示词工作流以及各类集成辅助。请遵循以下规范，确保贡献内容一致、可维护且可用于生产环境。

## 个人环境信息（维护者）

- **设备**：搭载 Apple 芯片的 Mac 电脑
- **Node.js 管理**：通过 Bun 进行安装与版本管理
- **Python 环境**：通过 uv 配置与管理
- **Git 代码托管平台**：GitHub
- **沟通语言**：所有后续沟通与回复使用中文

## 项目结构与模块组织
- `src/`：脚本复用的核心工具（API Key 加载、文本格式化、音频切分等）。
- `scripts/`：面向具体任务的 CLI（音频转写、Gemini 翻译、YouTube 下载等）；每个脚本依赖以 `pyproject.toml` 为准。
- `prompt/`、`information_anlaysis/`、`mermaid/`：用于提示词工程、知识分析与图表的配套资产。
- `working/`：进行中输入/输出的临时工作区；提交前请清理临时文件。
- `archived/` 与 `jupyter-notebook/`：历史资料与探索性笔记本——运行时代码不要依赖这里的内容。

## 构建、测试与开发命令
```bash
python -m venv .venv && source .venv/bin/activate  # 本地 virtualenv
pip install -r requirements.txt                    # 安装运行依赖（如使用 uv，也可用 `uv sync`）
python main.py                                     # 环境冒烟测试
python scripts/chat_with_llm.py --mode zh          # 示例：使用 working/input.md 跑一遍聊天流水线
```
请从仓库根目录运行脚本，以保证相对导入无需额外的 `PYTHONPATH` 配置即可正常工作。

## 代码风格与命名约定
- 使用 4 空格缩进、`snake_case` 的模块/函数命名，以及清晰的 docstring（在有帮助时可中英双语，语气保持与现有一致）。
- 共享逻辑请放在 `src/`；`scripts/` 应保持为薄的编排层，并通过 `argparse` 提供入口。
- 为新增的对外函数补充类型标注，并用 `pathlib.Path` 校验 I/O 路径。
- 不要硬编码密钥/配置——通过 `src.helper.get_api_key()` / `get_base_url()` 加载。

## 测试规范
- 优先为新增模块在 `tests/` 目录下补充轻量级 `pytest` 用例；文件命名为 `test_<feature>.py`。
- 对 CLI 工具，建议结合单元测试与样例夹具（可放在 `working/` 或 `examples/` 子目录），并在 PR 中记录手动验证步骤。
- 新增流式交互时，请分享一次可复现的输出记录，便于评审在不复跑的情况下确认行为。

## Commit 与 Pull Request 规范
- 沿用现有简短、祈使句风格的摘要（例如 `Add Skilljar downloader`、用于日期投放的 `20250918-mac`）；如有 issue，请在合适位置引用 ID。
- 保持提交聚焦；较大特性应拆分为多个逻辑清晰的提交。
- PR 需描述变更内容，列出验证步骤（运行了哪些命令/测试），并注明所需 API Key 或配置文件。
- 修改面向用户的产物或生成文档时，请提供变更前后上下文或截图。

## 安全与配置建议
- 凭据请存放在本地 `.env`，严禁提交密钥；新增环境变量键请在 PR 中说明。
- 引入新集成时，请检查添加到 `pyproject.toml` 的依赖许可证兼容性，并尽量固定精确版本。