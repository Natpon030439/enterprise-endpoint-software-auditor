from scanner import get_installed_software

print("=" * 70)
print("Enterprise Endpoint Software Auditor")
print("=" * 70)

software = get_installed_software()

for i, app in enumerate(software, start=1):
    print(f"{i:3}. {app['name']}")
    print(f"     Version  : {app['version']}")
    print(f"     Publisher: {app['publisher']}")
    print()

print("=" * 70)
print(f"Total Installed Software : {len(software)}")
