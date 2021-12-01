with import <nixpkgs> {};

let
  py = pkgs.python38;
in
stdenv.mkDerivation rec {
  name = "python-environment";

  buildInputs = with py.pkgs; [
    py
    py.pkgs.pip
    py.pkgs.numpy
  ];

  shellHook = ''
    set -h
  '';
}
