import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from links import linkedin_urls,linkedin_degrees_second , linkedin_degrees_third
from config import li_username, li_password,chrome_driver_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/")
driver.find_element_by_name('session_key').send_keys(li_username)
driver.find_element_by_name('session_password').send_keys(li_password)
driver.find_element_by_id('login-submit').click()


class connect():

    def search_results(self,url):

        try:
            url = url.replace(',', '%2C')
        except:
                pass
        try:
            url = url.replace('&', ' %26')
        except:
            pass
        linkedin_handle = url

        try:

            url = "https://www.linkedin.com/search/results/index/?keywords={0}&origin=GLOBAL_SEARCH_HEADER".format(url)
            driver.get(url)
            total_search_results = []
            total_search_results = driver.find_elements_by_class_name("actor-name")
            print("Total search results")
            print(len(total_search_results))
            connect.total_results(len(total_search_results))
            
        except:
            print('ERROR: Invalid URL:' + url)
            pass

    @staticmethod
    def total_results(results):
            if results == 1:
                try:
                    driver.execute_script('document.getElementsByClassName("name actor-name")[0].click();')
                    time.sleep(5)
                except Exception as e:
                    print(e)
                    driver.execute_script('document.getElementsByClassName("name actor-name")[0].click();')
                try:
                    name = WebDriverWait(driver, 50).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "pv-top-card-section__name"))
                        )
                    print("Name of person")
                    print(name.text)
                except Exception as e:
                    print("refreshing")
                    driver.find_element_by_name("s").sendKeys(Keys.F5)
                    # driver.refresh()
                    
                    driver.execute_script('document.getElementsByClassName("name actor-name")[0].click();')
                    name = WebDriverWait(driver, 50).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "pv-top-card-section__name"))
                        )
                    print("Name of person")
                    print(name.text)
                try:
                    degree = WebDriverWait(driver, 50).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "dist-value"))
                    )
                    print("Degree of connection")
                    print(degree.text)
                    connect.degree_of_connection(degree.text,name)
                except Exception as e:
                    print(e)
            
            if results > 1:
                try:
                    name = WebDriverWait(driver, 50).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "pv-top-card-section__name"))
                    )
                    print("Name of person")
                    print(name.text)
                except Exception as e:
                    
                    print("Refreshing")
                    driver.find_element_by_name("s").sendKeys(Keys.F5)
                    
                   # driver.refresh()
                    name = WebDriverWait(driver, 50).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "pv-top-card-section__name"))
                        )
                    print("Name of person")
                    print(name.text) 
                try:
                    degree = WebDriverWait(driver, 50).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "dist-value"))
                    )
                    print("Degree of connection")
                    print(degree.text)
                    connect.degree_of_connection(degree.text,name)
                except Exception as e:
                    print(e)
               

    @staticmethod
    def degree_of_connection(degree,name):
        if degree == "2nd":
            try:

                element = WebDriverWait(driver,50).until(
                    EC.presence_of_element_located((By.CLASS_NAME,"pv-highlight-entity__secondary-text"))
                )
                print("Highlights of profile")
                print(element.text)
                try :
                   # _,_, highlights = element.text.split("\n")
                    print("names of mutual connection")
                    print(element.text.split("know")[1])
                    second_message = element.text.split("know")[1]
                except Exception as e :
                    second_message = ''
                    pass

                total_connections = WebDriverWait(driver, 50).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "pv-top-card-v2-section__connections"))
                     )
                print("Total no of connections of person")
                print(total_connections.text)
                total_connections_person=total_connections.text.split(" ")[0]
                total_connections_of_person=total_connections_person.split("+")[0]
                connect.total_connections(total_connections_of_person, degree, name, second_message)

            except Exception as e:
                    print(e)
        if degree == "3rd" or len(degree.strip()) == 0:
            try:
                total_connections = WebDriverWait(driver, 50).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "pv-top-card-v2-section__connections"))
                         )
                print("Total no of connections of person")
                print(total_connections.text.split(" ")[0])
                total_connections_person = total_connections.text.split(" ")[0]
                total_connections_of_person = total_connections_person.split("+")[0]
                connect.total_connections(total_connections_of_person, degree, name)
            except Exception as e:
                        print(e)


    @staticmethod
    def total_connections(connections,degree,name,second_message=None):
        if degree == "2nd":
            if int(connections) > 100 :
                        
                try:
                    connect_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "pv-s-profile-actions--connect"))
                         )

                    connect_button.click()
                    try:

                        driver.execute_script(
                                "document.getElementsByClassName('button-secondary-large mr1')[0].click();")
                        row = linkedin_degrees_second[0]
                        names = row.split(",")[0]
                        msg = row.replace(names, name.text.split(" ")[0])
                        mes = msg.replace("<Person1, Person2>",second_message)
                        driver.find_element_by_name('message').send_keys(mes)
                        time.sleep(5)
                        driver.execute_script(
                                "document.getElementsByClassName('button-secondary-large-muted mr1')[0].click();")
                    except Exception as e:
                        print(e)

                    time.sleep(5)
                    print("there")
                except Exception as e:
                    try:
                        driver.execute_script(
                                    "document.getElementsByClassName('pv-s-profile-actions__overflow-toggle')[0].click();")
                        driver.execute_script(
                                    "document.getElementsByClassName('pv-s-profile-actions--connect')[0].click();")
                        driver.execute_script(
                                    "document.getElementsByClassName('button-secondary-large mr1')[0].click();")
                        row = linkedin_degrees_second[0]
                        names = row.split(",")[0]
                        msg = row.replace(names, name.text.split(" ")[0])
                        mes = msg.replace("<Person1, Person2>",second_message)
                        driver.find_element_by_name('message').send_keys(mes)
                        time.sleep(5)
                        driver.execute_script(
                                    "document.getElementsByClassName('button-secondary-large-muted mr1')[0].click();")

                    except Exception as e:
                            print("You may already connected or already sent request to user")
            else:
                        print("Profile have less than 100 connections so it may be fake")
        
        if degree == "3rd" or len(degree.strip()) == 0:
            if int(connections)>100 :

                try:
                    connect_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "pv-s-profile-actions--connect"))
                         )

                    connect_button.click()
                    try:

                        driver.execute_script(
                                "document.getElementsByClassName('button-secondary-large mr1')[0].click();")
                        row = linkedin_degrees_third[0]
                        names = row.split(",")[0]
                        msg = row.replace(names, name.text.split(" ")[0])
                        driver.find_element_by_name('message').send_keys(msg)
                        time.sleep(5)
                        driver.execute_script(
                                "document.getElementsByClassName('button-tertiary-large-muted mr1')[0].click();")
                    except Exception as e:
                        print(e)

                    time.sleep(5)

                except Exception as e:
                    try:
                        driver.execute_script(
                                    "document.getElementsByClassName('pv-s-profile-actions__overflow-toggle')[0].click();")
                        driver.execute_script(
                                    "document.getElementsByClassName('pv-s-profile-actions--connect')[0].click();")
                        driver.execute_script(
                                    "document.getElementsByClassName('button-secondary-large mr1')[0].click();")
                        row = linkedin_degrees_third[0]
                        names = row.split(",")[0]
                        msg = row.replace(names, name.text.split(" ")[0])
                        driver.find_element_by_name('message').send_keys(msg)
                        time.sleep(5)
                        try:
                           
                            email = driver.find_element_by_id('email')
                            print("email")
                           
                            WebDriverWait(driver, 50).until(lambda driver: len(driver.find_element_by_id("email").get_attribute("value")) > 20)
                            print("Email_correct")
                            driver.execute_script(
                                "document.getElementsByClassName('button-secondary-large-muted mr1')[0].click();")
                        except Exception as e:

                            driver.execute_script(
                                "document.getElementsByClassName('button-secondary-large-muted mr1')[0].click();")


                    except Exception as e:
                        print("You may already connected or already sent request to user")

            else:
                        print("Profile have less than 100 connections so it may be fake")


for url in linkedin_urls:
    cn = connect()
    cn.search_results(url)
driver.quit()