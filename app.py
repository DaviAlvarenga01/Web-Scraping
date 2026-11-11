import requests

def fetch_page():
    url = " https://lista.mercadolivre.com.br/3d?matt_tool=28082595&matt_word=Default_URL_MLB&matt_source=google&matt_campaign_id=11615372280&matt_ad_group_id=112431201359&matt_match_type=p&matt_network=g&matt_device=c&matt_creative=479783060301&matt_keyword=3d%20mercado%20livre&matt_ad_position=&matt_ad_type=&matt_merchant_id=&matt_product_id=&matt_product_partition_id=&matt_target_id=aud-1969798378558:kwd-1028474129456&cq_src=google_ads&cq_cmp=11615372280&cq_net=g&cq_plt=gp&cq_med=&gad_source=1&gad_campaignid=11615372280&gclid=Cj0KCQiAwdDXBhDuARIsAFdLukn7p3vDiSmobGGWXqtA-wlVeIes_22TW5iYvjsrimnZDpAo2LXOLCwaAnUHEALw_wcB "
    response = requests.get(url)
    return response.text
if __name__ == "__main__":
    content = fetch_page()
    print(content)

