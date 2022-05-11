let
  pkgs = import (fetchTarball("channel:nixpkgs-unstable")) { };
in pkgs.mkShell {
  buildInputs = with pkgs; [
    python39Packages.poetry
    python39Packages.ipykernel
    python39Packages.ipython
    python39Packages.pip
    python39Packages.black
  ];
}
