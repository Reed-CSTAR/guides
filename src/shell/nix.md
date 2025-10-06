# Nix Cheatsheet

You can use **Nix** to install additional software anywhere Nix itself is
installed.

- To search for a package:
  ```text
  $ nix search nixpkgs hello
  * legacyPackages.x86_64-linux.hello (2.12.1)
  A program that produces a familiar, friendly greeting
  ```

- To install a package:
  ```text
  $ nix profile install nixpkgs#hello
  ```

- To start a temporary shell without installing a package:
  ```text
  $ nix shell nixpkgs#hello
  $ hello
  Hello, world!
  ```

- To list installed packages:
  ```text
  $ nix profile list
  Index:              0
  Flake attribute:    legacyPackages.x86_64-linux.hello
  Original flake URL: flake:nixpkgs
  Locked flake URL:   github:NixOS/nixpkgs/2646b294a146df2781b1ca49092450e8a32814e1
  Store paths:        /nix/store/z6hzxgy21zimj58xhy06f2f49qgy06gg-hello-2.12.1
  ```

- To uninstall a package by index:
  ```text
  nix profile remove 0
  removing 'flake:nixpkgs#legacyPackages.x86_64-linux.hello'
  ```

For more information about Nix, you can look at [Zero to Nix](https://zero-to-nix.com).
