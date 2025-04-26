import speedtest
import os

def run_speedtest():
    print("\n🚀 Processing speed test 🚀\n")
    
    st = speedtest.Speedtest() # speedtest object
    
    st.get_best_server() # best server
    server = st.best
    
    isp = st.config['client']['isp']
    ping = round(st.results.ping)
    # Download speed
    print("⬇️  Download speed test...")
    download_speed = st.download() / 1_048_576  # unit:  Mbps
    # Upload speed
    print("⬆️  Upload speed test...")
    upload_speed = st.upload(pre_allocate=False) / 1_048_576  # unit: Mbps
    
    
    # Print results
    print(f"🌍 Connectted with most optimal server:")
    print(f"📌 Host: {server['host']}")
    print(f"🏙️  Location: {server['name']}, {server['country']}")
    print(f"🏢 Provider: {server['sponsor']}")
    print(f" ISP: {isp}\n")

    print(f"📶 Ping: {ping} ms")
    print(f"✅ Download speed: {download_speed:.2f} Mbps")
    print(f"✅ Upload speed: {upload_speed:.2f} Mbps")
    print("\n🎯 Speedtest completed! 🚀")

    # Functie om resultaten op te slaan
    def save_info():
        directory = "saves"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        custom_name = input("Enter custom filename (without extension): ").strip()
        if custom_name.endswith(".txt") or custom_name.endswith(".json") or custom_name.endswith(".csv") or custom_name.endswith(".xml"):
            custom_name = custom_name[:-4]       
        
        filename = os.path.join(directory, f"{custom_name}.txt" if custom_name else "speedtest_result.txt")

        with open(filename, "w") as file:
            file.write(f"Host: {server['host']}\n")
            file.write(f"Location: {server['name']}, {server['country']}\n")
            file.write(f"Provider: {server['sponsor']}\n")
            file.write(f"ISP: {isp}\n")
            file.write(f"Ping: {ping} ms\n")
            file.write(f"Download speed: {download_speed:.2f} Mbps\n")
            file.write(f"Upload speed: {upload_speed:.2f} Mbps\n")
        
        print(f"\n📁 Results saved in: {filename}")

    # Sla de resultaten op
    save = input("Do you want to save the results? (y/n): ").strip().lower()
    if save == "y":
        save_info()

# Run de speedtest
run_speedtest()
