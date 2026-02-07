# Changelog

All notable changes to the Subterfuge repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Interactive menu mode (choose specific effects or scenarios)
- Achievement/stats tracking across sessions
- Database queries with fake results
- Sound effects (terminal beeps)
- Command-line arguments for different modes
- Save/replay sequences

---

## [2026-02-07] - Version Tracking Standards

### Added
- `__version__ = "3.0.0"` added to `subterfuge.py` per workspace standard (Python convention)
- `set ScriptVersion=1.0.0` added to `run_subterfuge.bat`
- `CHANGELOG.md` with full version history

---

## Main Script

### subterfuge.py

#### [3.0.0] - 2025-12-14 - "Movie Magic Edition"

##### Added
- WarGames WOPR dialogue ("Shall we play a game?" complete sequence)
- Radar sweep animation with contact detection, bearings, and range
- 7 animated spinner styles (dots, lines, arrows, pulses, boxes, circles, blocks)
- ASCII art gallery (WOPR, Matrix, Skull, Cyber banners)
- Themed scenarios: WarGames, The Matrix, Cyberpunk/Mr. Robot

#### [2.0.0] - 2025-11-23 - Enhancement Phase

##### Added
- Network scanner with port scanning, service detection, vulnerability assessment (CVE refs)
- Terminal breach sequence (5 access levels: Public > User > Admin > Root > Kernel)
- Glitch effect (text distortion animation)
- Data stream interception (packet capture simulation with checksums)
- Binary cascade (falling binary numbers)

#### [1.0.0] - 2025-11-01 - Initial Build

##### Added
- Core HackerSimulator class
- Matrix rain effect (falling green/cyan characters)
- Animated progress bars with random operations
- Scrolling code snippets (Python, JS, SQL, Docker)
- Fake log messages with timestamps and IPs
- System stats monitor (CPU, memory, network, threads)
- File operation simulations (encrypt, decrypt, compile)
- Continuous random operation loop
- Graceful Ctrl+C handling
- ANSI color support
- Windows UTF-8 console encoding

---

## Launcher

### run_subterfuge.bat

#### [1.0.0] - 2025-11-01

##### Added
- Windows batch launcher for subterfuge.py

---

## Repository-Level Changes

### [2026-02-07]
- Added version tracking to all scripts
- Added CHANGELOG.md

### [2025-12-14]
- v3.0.0 "Movie Magic Edition" - WarGames, themed scenarios, ASCII art

### [2025-11-23]
- v2.0.0 - Network scanning, terminal breach, advanced animations

### [2025-11-01]
- Initial repository structure
- Core hacker simulator with visual effects

---

## Technical Notes

- **Language**: Python 3 (standard library only, no dependencies)
- **Colors**: ANSI escape codes
- **Platform**: Cross-platform (Windows, Linux, macOS)
- **Architecture**: Single-file, class-based (HackerSimulator)

---

## Related Documentation

- [SUBTERFUGE.md](SUBTERFUGE.md) - Development notes and feature history
- [README.md](README.md) - User documentation
- [../OPERATIONS.md](../OPERATIONS.md) - Workspace standards
