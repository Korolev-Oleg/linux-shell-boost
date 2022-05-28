#!/usr/bin/python3
import os
import platform
from dataclasses import dataclass

def get_os_name():
    match platform.version().lower():
        case 'ubuntu':
            return 'ubuntu'
        case 'debian':
            return 'debian'
        case 'fedora': 
            return 'fedora'
        case 'centos':
            return 'centos'

def get_default_package_manager(os_name):
    match os_name:
        case 'ubuntu':
            return 'apt'
        case 'debian':
            return 'apt'
        case 'fedora':
            return 'dnf'
        case 'centos':
            return 'apt'



class Install:
    package_manager: str
    web_manager: str
    os_name: str

    def __init__(self):
        self.os_name = get_os_name()
        self.package_manager = get_default_package_manager(self.os_name)
        self.web_manager = 'curl'
        os.system(f"""
            sudo {self.package_manager} update
            sudo {self.package_manager} install -y curl
        """)

    def zsh(self):
        os.system(f"""
            sudo {self.package_manager} install -y zsh
        """)

    def oh_my_zsh(self):
        os.system(f"""
            sh -c "$({self.web_manager} -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
        """)

    def default_zsh_plugins(self):
        os.system("""""")

    def hack_nerdfonts(self):
        os.system("""""")

    def color_ls(self):
        os.system("""""")

    def tmux(self):
        os.system("""""")

    def neovim(self):
        os.system("""""")

    def ruby(self):
        if self.os_name:
            os.system("""
            
            """)

install = Install()

@dataclass
class Config:
    INSTALL_ZSH=install.zsh
    INSTALL_OH_MY_ZSH=install.oh_my_zsh
    INSTALL_DEFAULT_ZSH_PLUGINS=install.default_zsh_plugins
    INSTALL_HACK_NERDFONTS=install.hack_nerdfonts # fonts
    INSTALL_COLOR_LS=install.color_ls
    INSTALL_TMUX=install.tmux
    INSTALL_NEOVIM=install.neovim # nvim

    def list_attrs__(self) -> list:
        return [attr for attr in sorted(dir(Config)) if '__' not in attr]


config = Config()

def ask_user():
    for attr in config.list_attrs__():
        title = attr.capitalize().replace('_', ' ')
        choise = input(title + '? (y/n) ') in ('y', 'yes', '1', '')
        if not choise:
            setattr(config, attr, choise)


def do_install():
    ask_user()
    for attr in config.list_attrs__():
        install = getattr(config, attr)
        if install:
            install()


if __name__ == '__main__':
    do_install() 
