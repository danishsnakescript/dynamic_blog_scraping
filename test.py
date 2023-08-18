def InsideBlog(Multiple_links):
    for z in Multiple_links:
        print(z)
        session = requests.Session()
        data3 = session.get(z)
        soup3 = BeautifulSoup(data3.text, "html.parser")
        body = soup3.find('body')
        if body:
            for tag_name in ['header', 'footer']:
                header_footer_elements = body.find_all(tag_name)
                for element in header_footer_elements:
                    element.extract()

            for div_class in ['header', 'footer']:
                div_elements = body.find_all('div', class_=div_class)
                for div_element in div_elements:
                    div_element.extract()

            heading_tags = ['h1', 'h2', 'h3', 'h4','h5','h6']

            for tag in heading_tags:
                heading_elements = soup3.find_all(tag)
                for head in heading_elements:
                    print("Heading:", head.text)

                    # Find the first paragraph tag after the heading
                    sibling = head.find_next_sibling()
                    while sibling:
                        if sibling.name == 'p':
                            print("Paragraph:", sibling.text)
                            break
                        sibling = sibling.find_next_sibling()

                    if not sibling:
                        # If no immediate sibling p tag, find the first p tag after the heading
                        first_p_after_heading = head.find_next('p')
                        if first_p_after_heading:
                            print("Paragraph:", first_p_after_heading.text)
                        else:
                            print("No paragraph found")

                    print("\n")

def Inside(links):
    # blog_keyword = ['blog','blogs','BLOG','BLOGS','Blog','Blogs','post_','Post_','POST_','post','Post','Post','article','Article','ARTICLES']
    blog_keyword = ['blog','blogs','BLOG','BLOGS','Blog','Blogs','post_','Post_','single.php']
    Multiple_links = []
    for i in links:
        session = requests.Session()
        data2 = session.get(i)
        if data2.status_code == 200:
            soup2 = BeautifulSoup(data2.text, "html.parser")
            body = soup2.find('body')
            if body:
                for tag_name in ['header', 'footer']:
                    header_footer_elements = body.find_all(tag_name)
                    for element in header_footer_elements:
                        element.extract()

                for div_class in ['header', 'footer']:
                    div_elements = body.find_all('div', class_=div_class)
                    for div_element in div_elements:
                        div_element.extract()
            anchor = body.find_all('a')          
            for a in anchor:
                a_link = a.get('href')
                if a_link:
                    for k in blog_keyword:
                        if k in a_link:
                            if a_link not in Multiple_links:
                                Multiple_links.append(a_link)
        
        else:
            print(f"Error fetching {i}: Status Code {data2.status_code}")

        filtered_links = []
        filtered_links = [link for link in Multiple_links if link.startswith('https://')]
        if not filtered_links:
                    for link in Multiple_links:
                        for keyword in blog_keyword:
                            if keyword in link:
                                final_url = f"{url}{link}"
                                filtered_links.append(final_url)
        return filtered_links
    

from bs4 import BeautifulSoup
import requests
import pandas  
def blog_links(url):
    session = requests.Session()
    data = session.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    all_links = soup.find_all('a')  
    # blog_keywords = ['blog','blogs','BLOG','BLOGS','Blog','Blogs','post_','Post_','POST_','post','posts','Post','Posts','POST','POSTS','article','Article','ARTICLE','articles','Articles','ARTICLES',"Write","Writing","Content","Writer","Publish","Published","Publishing","Author","Authors","Blogger","Blogging","Written","Read","Reading","Editorial","Editor","Online","Platform","Story","Stories","Journal","Journalism","Opinion","Opinions","Commentary","Update","Updates","Insight","Insights","Informative","Inform","News","Newsworthy","Share","Sharing","write","writing","content","writer","publish","published","publishing","author","authors","blogger","blogging","written","read","reading","editorial","editor","online","platform","story", "stories","journal","journalism","opinion","opinions","commentary","update","updates","insight","insights","informative","inform","news","newsworthy","share","sharing"]
    blog_keywords = ['blog','blogs','BLOG','BLOGS','Blog','Blogs','post_','Post_','single.php']
    Links = []   
    for a_tag in all_links:
        link = a_tag.get('href')
        if link:
            for i in blog_keywords:
                if i in link:
                    if link not in Links:
                        if "https://www." in link:
                            link = link.replace("https://www.", "https://")
                        Links.append(link)
    filtered_links = []
    filtered_links = [link for link in Links if link.startswith('https://') and any(keyword in link for keyword in blog_keywords)]
    if not filtered_links:
        filtered_links = [link for link in Links if link.startswith('https://') and any(keyword in link for keyword in blog_keywords) and link.endswith('.com')]
    if not filtered_links:
        for link in Links:
            for keyword in blog_keywords:
                if keyword in link:
                    final_url = f"{url}{link}"
                    filtered_links.append(final_url)

    return filtered_links

url = input("enter URL: ")
links = blog_links(url)
# print(links)
multiple_links = Inside(links)
# print(multiple_links)
fullBlog = InsideBlog(multiple_links)
print(fullBlog)
