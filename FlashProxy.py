import requests
import sys
import time


class proxy_checker:
    def __init__(self):
        self.sec = time.gmtime().tm_sec
        self.min = time.gmtime().tm_min
        self.hour = time.gmtime().tm_hour
        print("Program Started: {}\n".format(
            self.print_time(self.sec, self.min, self.hour)))
        self.commonflag = 0
        self.read(self.commonflag)
        self.siteflag = 0

    def proxy_type(self):
        print("[01] HTTP / HTTPS ")
        print("[02] SOC0KS4")
        print("[03] SOCKS5\n")
        select = input("[FlashProxy$] ")
        if select == "01" or select == "1":
            proxy_type = "http"
            print("[01] HTTP / HTTPS <- SELECTED")
            print("[02] SOCKS4")
            print("[03] SOCKS5")
        elif select == "02" or select == "2":
            proxy_type = "socks4"
            print("[01] HTTP / HTTPS")
            print("[02] SOCKS4 <- SELECTED")
            print("[03] SOCKS5")
        elif select == "03" or select == "3":
            proxy_type = "socks5"
            print("[01] HTTP / HTTPS ")
            print("[02] SOCKS4")
            print("[03] SOCKS5 <- SELECTED")

        else:
            print("Program Terminated! | {}".format(
                self.print_time(self.sec, self.min, self.hour)))
            sys.exit("Invalid Option!! XE")
        return proxy_type

    def write(self, proxy, proxy_type):
        with open("live_{}_proxies.txt".format(proxy_type), "a") as line:
            line.write("{}\n".format(proxy))

    def read(self, commonflag):
        try:
            proxytype = self.proxy_type()

        # Commonflag is a flag which makes sure select_website() is only run once!

            proxylist = input("\nInput Proxy list\n[FlashProxy$]")
            with open(proxylist, "r") as proxies:
                proxyset = [proxy.rstrip() for proxy in proxies]
                for proxylocation, proxy in enumerate(proxyset, 1):
                    if self.commonflag == 0:
                        self.select_websites()
                        self.commonflag = 1
                    else:
                        self.check(proxy, proxytype, proxylocation)
        except KeyboardInterrupt:
            print("Program Terminated! | {}".format(
                self.print_time(self.sec, self.min, self.hour)))
            sys.exit("Program Stopped!")
        except FileNotFoundError:
            print("\nProgram Terminated! | {}".format(
                self.print_time(self.sec, self.min, self.hour)))
            sys.exit("File not Found!")

    def select_websites(self):
        global siteflag
        print("\nDEFAULT WEBSITE: https://canihazip.com/s")
        print("[01].https://www.google.com")
        print("[02].https://wwww.netflix.com")
        select = input("\nSelect an option\n[FlashProxy$]")
        if select == "01" or select == "1":
            print("[01].https://www.google.com")
            siteflag = 1
        elif select == "02" or select == "2":
            print("[02].https://wwww.netflix.com")
            siteflag = 2
        elif select == " "or select == "":
            print("https://canihazip.com/s")
            siteflag = 0
        return siteflag

    def check(self, proxy, proxytype, proxylocation):
        result = {'http': '{}://{}'.format(proxytype, proxy)}
        try:
            if siteflag == 1:
                link = "https://www.google.com <- SELECTED"
                success_keyword = """ <input value="I'm Feeling Lucky" """
            elif siteflag == 2:
                link = "https://www.netflix.com <- SELECTED"
                success_keyword = """<div class="our-story-cta-container">"""
            elif siteflag == 0:
                success_keyword = proxy.split(":")[0]
                link = "https://canihazip.com/s <- SELECTED"
            print(link)
            source = requests.get(link,
                                  proxies=result, timeout=3)

#            print("Status Code: {}".format(source.status_code))

            if source.status_code == 200 or success_keyword in source.text:
                self.write(proxy, proxytype)
                print("LIVE PROXY: {} | {} | {} | {}".format(
                    proxy, proxytype[0], proxylocation, self.print_time(self.sec, self.min, self.hour)))
            else:
                print("DEAD PROXY: {} | {} | {} | {}".format(
                    proxy, proxytype[0], proxylocation, self.print_time(self.sec, self.min, self.hour)))
        except KeyboardInterrupt:
            print("Program Terminated! | {}".format(
                self.print_time(self.sec, self.min, self.hour)))
            sys.exit("Program Stopped!")
        except ConnectionError:
            print("Program Terminated! | {}".format(
                self.print_time(self.sec, self.min, self.hour)))
            sys.exit("Connection Error!")
        except:
            pass

    def print_time(self, sec, min, hour):
        return ("{}:{}:{}".format(time.gmtime().tm_hour - hour,
                                  time.gmtime().tm_min - min, time.gmtime().tm_sec - sec))


if __name__ == "__main__":
    proxy_checker()
