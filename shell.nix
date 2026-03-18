{pkgs ? import (import ./npins).nixpkgs {}}:
with pkgs;
  mkShellNoCC {
    packages = [
      nil
      alejandra
      pyrefly
      ruff
      (python3.withPackages (p:
        with p; [
          fastapi
        ]))
    ];
  }
