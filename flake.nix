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
          nodemon --watch . --ext py --exec "clear && poetry run main"
        '';
        testwatcher = pkgs.writeShellScriptBin "testwatcher" ''
          nodemon --watch . --ext py --exec "clear && poetry run pytest"
        '';
        buildInputs = [
          watcher
          testwatcher
          pkgs.fish
          pkgs.python314
          pkgs.poetry
          pkgs.nodemon
          pkgs.rclone
        ];
      in
      {
        devShells = {
          default =
            with pkgs;
            mkShell {
              buildInputs = buildInputs;
              shellHook = ''
                fish -C "source ./.venv/bin/activate.fish"
              '';
            };
          ci =
            with pkgs;
            mkShell {
              buildInputs = buildInputs;
              shellHook = ''
                source ./.venv/bin/activate
              '';
            };
        };
      }
    );
}
