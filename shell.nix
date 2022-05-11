let
  pkgs = import (fetchTarball("channel:nixpkgs-unstable")) { };
in pkgs.mkShell {
  buildInputs = with pkgs; [
    python39Packages.poetry
  ];
}
