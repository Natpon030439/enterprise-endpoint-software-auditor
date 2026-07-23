import winreg


def get_installed_software():
    software = []

    registry_paths = [
        (winreg.HKEY_LOCAL_MACHINE,
         r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),

        (winreg.HKEY_LOCAL_MACHINE,
         r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),

        (winreg.HKEY_CURRENT_USER,
         r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
    ]

    for hive, path in registry_paths:
        try:
            key = winreg.OpenKey(hive, path)

            for i in range(winreg.QueryInfoKey(key)[0]):
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    subkey = winreg.OpenKey(key, subkey_name)

                    try:
                        name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    except FileNotFoundError:
                        continue

                    try:
                        version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                    except FileNotFoundError:
                        version = ""

                    try:
                        publisher = winreg.QueryValueEx(subkey, "Publisher")[0]
                    except FileNotFoundError:
                        publisher = ""

                    software.append({
                        "name": name,
                        "version": version,
                        "publisher": publisher
                    })

                except Exception:
                    pass

        except Exception:
            pass

    return sorted(software, key=lambda x: x["name"].lower())
