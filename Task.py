import platform
import subprocess
import psutil
import cpuinfo
import screeninfo
import uuid
import requests

# Function to get installed software on Windows
def get_installed_software_windows():
    try:
        command = 'wmic product get name'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        output_str = output.decode('utf-8')
        software_list = [line.strip() for line in output_str.split('\n') if line.strip()]
        return set(software_list)
    except Exception as e:
        return f"Error: {e}"

# Function to get screen resolution
def get_screen_resolution():
    try:
        screen = screeninfo.get_monitors()[0]
        return f"{screen.width}x{screen.height}"
    except Exception as e:
        return f"Error: {e}"

# Function to get CPU information
def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    cpu_model = info['brand_raw']
    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    return cpu_model, cores, threads

# Function to get GPU information
def get_gpu_info():
    try:
        import GPUtil
        gpu = GPUtil.getGPUs()[0]
        return gpu.name
    except ImportError:
        return "GPUtil library not installed"

# Function to get RAM size
def get_ram_size():
    ram = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    return ram

# Function to get screen size
def get_screen_size():
    try:
        screen = screeninfo.get_monitors()[0]
        diagonal_size = round((screen.width**2 + screen.height**2)**0.5 / 25.4, 2)
        return f"{diagonal_size} inch"
    except Exception as e:
        return f"Error: {e}"

# Function to get MAC address
def get_mac_address():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    return mac_address

# Function to get public IP address
def get_public_ip_address():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        data = response.json()
        return data['ip']
    except requests.RequestException:
        return "Unable to fetch public IP address"

# Function to get Windows version
def get_windows_version():
    return platform.version()

# Main code to print system details
if __name__ == "__main__":
    # Installed Software
    installed_software = get_installed_software_windows()
    print("Installed Software:", installed_software)

    # Screen Resolution
    screen_resolution = get_screen_resolution()
    print("Screen Resolution:", screen_resolution)

    # CPU Information
    cpu_model, cores, threads = get_cpu_info()
    print("CPU Model:", cpu_model)
    print("Number of Cores:", cores)
    print("Number of Threads:", threads)

    # GPU Information
    gpu_model = get_gpu_info()
    print("GPU Model:", gpu_model)

    # RAM Size
    ram_size = get_ram_size()
    print("RAM Size:", round(ram_size, 2), "GB")

    # Screen Size
    screen_size = get_screen_size()
    print("Screen Size:", screen_size)

    # MAC Address
    mac_address = get_mac_address()
    print("MAC Address:", mac_address)

    # Public IP Address
    public_ip_address = get_public_ip_address()
    print("Public IP Address:", public_ip_address)

    # Windows Version
    windows_version = get_windows_version()
    print("Windows Version:", windows_version)
