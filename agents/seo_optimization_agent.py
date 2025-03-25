import re

def optimize_seo(content):
    keywords = ["AI in hiring", "HR technology", "future of work", "employee retention"]
    keyword_count = {kw: content.lower().count(kw) for kw in keywords}
    
    # Basic SEO Improvements
    optimized_content = content
    for kw in keywords:
        optimized_content = re.sub(rf'\b({kw})\b', rf'**\1**', optimized_content, flags=re.IGNORECASE)

    return optimized_content, keyword_count

if __name__ == "__main__":
    content = "AI in hiring is transforming the future of work..."
    optimized_content, kw_count = optimize_seo(content)
    print(optimized_content)
    print(kw_count)
