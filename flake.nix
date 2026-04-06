{
  description = "NRP Scraper";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        bin = "./.venv/bin";
        pkgs = import nixpkgs { inherit system; };
        watcher = pkgs.writeShellScriptBin "watcher" ''
          nodemon --watch . --ext py --exec "clear && ${bin}/python3.14 main.py"
        '';
        testwatcher = pkgs.writeShellScriptBin "testwatcher" ''
          nodemon --watch . --ext py --exec "clear && ${bin}/pytest"
        '';
      in
      {
        devShells.default =
          with pkgs;
          mkShell {
            buildInputs = [
              watcher
              testwatcher
              pkgs.fish
              pkgs.python314
              pkgs.poetry
              pkgs.nodemon
            ];
            shellHook = ''
              fish -C "source ./.venv/bin/activate.fish"
            '';
          };
      }
    );
}
