{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python310   # or any other Python version
    pkgs.python310Packages.pip
    pkgs.python310Packages.virtualenv
  ];

  # Automatically set up and activate a virtual environment when entering the shell
  shellHook = ''
    if [ ! -d .venv ]; then
      python -m venv .venv
    fi
    source .venv/bin/activate
  '';
}
