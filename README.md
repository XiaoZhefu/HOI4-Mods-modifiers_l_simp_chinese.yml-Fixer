# HOI4 Mods - modifiers_l_simp_chinese.yml Fixer

## 简介

这是一个用于批量补全钢丝Mod中buff汉化文件 `modifiers_l_simp_chinese.yml` 文本图标缺失问题的工具。

## 文件说明

本项目包含以下文件：

- **`fix.py`**：主程序文件。
- **`modifiers_l_simp_chinese.yml`**：未修改的中文汉化文件（示例）。
- **`modifiers_l_simp_chinese_new.yml`**：修复后的中文汉化文件（示例）。
- **`modifiers_l_english.yml`**：英文参考文件，用于匹配图标描述（示例）。

## 使用方法

1. 确保文件夹内包含以下文件：
   - `fix.py`
   - `modifiers_l_simp_chinese.yml`
   - `modifiers_l_english.yml`

2. 运行 `fix.py`。

3. 程序运行结束后，会自动生成 `modifiers_l_simp_chinese_new.yml` 文件。

4. 将生成的 `modifiers_l_simp_chinese_new.yml` 重命名为 `modifiers_l_simp_chinese.yml`，并覆盖模组文件夹中的原文件。

## 注意事项

- **备份原文件**：覆盖原文件前，请务必备份 `modifiers_l_simp_chinese.yml`。

## 许可证

本项目遵循GNU GPLv3协议。
