from agents.research_agent import fetch_trending_hr_topics
from agents.content_planning_agent import generate_outline
from agents.content_generation_agent import generate_content
from agents.seo_optimization_agent import optimize_seo
from agents.review_agent import review_content
import markdown2

def save_blog(content, filename="blog_post"):
    with open(f"{filename}.md", "w", encoding="utf-8") as md_file:
        md_file.write(content)
    with open(f"{filename}.html", "w", encoding="utf-8") as html_file:
        html_file.write(markdown2.markdown(content))

def main():
    print("Fetching trending HR topics...")
    topic = fetch_trending_hr_topics()[0]  # Select the first trending topic

    print(f"Generating outline for: {topic}")
    outline = generate_outline(topic)

    print("Generating blog content...")
    content = generate_content(outline)

    print("Optimizing for SEO...")
    optimized_content, _ = optimize_seo(content)

    print("Reviewing content...")
    final_content = review_content(optimized_content)

    print("Saving blog post...")
    save_blog(final_content)

    print("Blog generation complete. Check output files.")

if __name__ == "__main__":
    main()
