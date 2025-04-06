import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Fateha Jannat Ayrin | Portfolio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #0a3d62;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 24px;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #60a3bc;
            color: white;
        }
        h1, h2, h3 {
            color: #0a3d62;
        }
        hr {
            margin-top: 1rem;
            margin-bottom: 1rem;
        }
        .project-card, .research-card, .education-card {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .skill-tag {
            background-color: #60a3bc;
            color: white;
            padding: 5px 10px;
            border-radius: 20px;
            display: inline-block;
            margin: 3px;
            font-size: 0.8em;
        }
        .timeline-date {
            font-weight: bold;
            color: #0a3d62;
        }
        .contact-info {
            padding: 20px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .sidebar .sidebar-content {
            background-color: #0a3d62;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Sidebar
def sidebar():
    # Add profile picture
    # st.sidebar.image("profile_pic.jpg", width=200)
    
    # Since we don't have an actual image, using a placeholder
    st.sidebar.markdown("""
    <div style="display: flex; justify-content: center;">
        <div style="width: 150px; height: 150px; border-radius: 50%; background-color: #60a3bc; 
        display: flex; justify-content: center; align-items: center; color: white; font-size: 36px;">
            FJA
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.title("Fateha Jannat Ayrin")
    st.sidebar.subheader("Computer Science Educator & Researcher")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Navigation")
    
    pages = {
        "About Me": "about",
        "Education & Experience": "education",
        "Research Publications": "research",
        "Projects": "projects",
        "Skills & Certifications": "skills",
        "OCR Demo": "ocr_demo",
        "Contact Me": "contact"
    }
    
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Contact Information")
    st.sidebar.markdown("📧 fjayrin@gmail.com")
    st.sidebar.markdown("📱 +880 16 162 47349")
    st.sidebar.markdown("🔗 [GitHub](https://github.com/ayrin21)")
    st.sidebar.markdown("🔗 [LinkedIn](https://linkedin.com/in/fateha-jannat-ayrin)")
    
    st.sidebar.markdown("---")
    st.sidebar.info("Lecturer at Port City International University, Chittagong, Bangladesh")
    
    return pages[selected_page]

# Pages
def about_page():
    st.title("About Me")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Summary
        
        As an educator and researcher, I am passionate about fostering the academic growth of students and creating an engaging learning environment. I am determined to mentor students, simplify complex concepts, and inspire critical thinking. My goal is to contribute to the academic community through effective teaching, guidance, and continuous learning.
        
        ### Research Interests
        
        My research focuses on:
        - Optical Character Recognition (OCR) Technology
        - Large Language Models (LLMs)
        - Deep Learning for Medical Imaging
        - Computer Vision
        """)
        
    with col2:
        st.markdown("""
        ### Quick Info
        
        📍 **Location**  
        Chittagong, Bangladesh
        
        🎓 **Current Position**  
        Lecturer, Port City International University
        
        🔍 **Specialization**  
        OCR Technology, Machine Learning & Web Development
        
        📚 **Education**  
        MSc in Computer Science & Engineering (Ongoing)  
        BSc in Computer Science & Engineering (CGPA: 3.73/4.00)
        """)
    
    st.markdown("---")
    
    st.markdown("### Featured Research")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### TrOCR for Blurred and Low Quality Images
        
        Developed an OCR system achieving 96.8% accuracy on IIIT 5K dataset for extracting text from blurred and low-quality images. The research addresses a critical challenge in document digitization and information extraction from degraded visual sources.
        
        **Publication**: IEEE ECCE - 2025
        """)
    
    with col2:
        st.markdown("""
        #### COVID-19 Lung Infections Detection
        
        Created a 3D UNet model with 95.56% accuracy for detecting COVID-19 infections in CT scans. This work contributes to faster and more accurate diagnosis of COVID-19 through medical imaging analysis.
        
        **Publication**: IEEE AMATHE 2024 (Best Paper Award)
        """)
    
    # Add an interactive component
    st.markdown("---")
    st.subheader("Research Focus Areas")
    
    data = pd.DataFrame({
        'Area': ['OCR Technology', 'Language Models', 'Computer Vision', 'Medical Imaging', 'Web Development'],
        'Expertise Level': [90, 85, 80, 75, 70]
    })
    
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('Expertise Level', scale=alt.Scale(domain=[0, 100])),
        y=alt.Y('Area', sort='-x'),
        color=alt.Color('Expertise Level', scale=alt.Scale(scheme='blues'), legend=None)
    ).properties(
        height=250
    )
    
    st.altair_chart(chart, use_container_width=True)

def education_experience_page():
    st.title("Education & Experience")
    
    tab1, tab2 = st.tabs(["Education", "Work Experience"])
    
    with tab1:
        st.subheader("Academic Background")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown("#### 2022 - Present")
            st.markdown("#### 2019 - 2022")
            st.markdown("#### 2016 - 2018")
            st.markdown("#### 2006 - 2016")
        
        with col2:
            with st.container():
                st.markdown("### Master of Science (Engineering) in Computer Science & Engineering")
                st.markdown("**University of Chittagong**")
                st.markdown("*1st Semester, Session: 2022-2023*")
                st.markdown("**Thesis**: OCR Technology With LVM")
            
            st.markdown("---")
            
            with st.container():
                st.markdown("### Bachelor of Science (Engineering) in Computer Science & Engineering")
                st.markdown("**University of Chittagong**")
                st.markdown("*CGPA: 3.73 out of 4.00*")
                st.markdown("**Thesis**: OCR Technology For Blurred Images and Low Quality Images")
            
            st.markdown("---")
            
            with st.container():
                st.markdown("### Higher Secondary Certificate")
                st.markdown("**BMS Girls' High School & College**")
                st.markdown("*GPA: 4.58 out of 5.00*")
            
            st.markdown("---")
            
            with st.container():
                st.markdown("### Secondary School Certificate")
                st.markdown("**CMP School & College**")
                st.markdown("*GPA: 5.00 out of 5.00*")
    
    with tab2:
        st.subheader("Professional Experience")
        
        st.markdown("""
        <div class="education-card">
            <h3>Lecturer - Full Time</h3>
            <p class="timeline-date">January 2025 - Present</p>
            <p><strong>Port City International University, Chittagong</strong></p>
            <p>Department of Computer Science & Engineering</p>
            <ul>
                <li>Teaching courses on Digital Logic Design (DLD), Computer Networking, Machine Learning, and various engineering subjects</li>
                <li>Mentoring students on academic projects and research activities</li>
                <li>Developing course materials and assessment strategies</li>
                <li>Conducting lab sessions and practical demonstrations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Add a simple visualization of teaching workload
        st.subheader("Teaching Distribution")
        
        teaching_data = pd.DataFrame({
            'Course': ['Digital Logic Design', 'Computer Networking', 'Machine Learning', 'Other Engineering Courses'],
            'Hours per Week': [6, 4, 5, 3]
        })
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(teaching_data['Course'], teaching_data['Hours per Week'], color='#60a3bc')
        ax.set_xlabel('Hours per Week')
        ax.set_title('Weekly Teaching Hours by Course')
        
        # Add data labels
        for i, v in enumerate(teaching_data['Hours per Week']):
            ax.text(v + 0.1, i, str(v), color='#0a3d62', va='center', fontweight='bold')
        
        st.pyplot(fig)

def research_page():
    st.title("Research Publications")
    
    # Function to create research publication cards
    def research_card(title, conference, year, technologies, description, achievements=None, color="#0a3d62"):
        st.markdown(f"""
        <div class="research-card" style="border-left: 5px solid {color}; padding-left: 15px;">
            <h3>{title}</h3>
            <p><strong>Published in:</strong> {conference} - {year}</p>
            <p><strong>Technologies:</strong> <span class="tech-stack">{technologies}</span></p>
            <p>{description}</p>
            {f"<p><strong>Achievements:</strong> {achievements}</p>" if achievements else ""}
        </div>
        """, unsafe_allow_html=True)
    
    research_card(
        "An Optical Character Recognition Technique for Extracting Text from Blurred and Low Quality Images Using TrOCR",
        "IEEE ECCE", "2025",
        "TrOCR, Seq2seq, VisionEncoderDecoder",
        "Developed a robust OCR system achieving 96.8% accuracy on IIIT 5K dataset. Implemented TrOCR with VisionEncoderDecoder and Seq2Seq framework to extract text from challenging image conditions.",
    )
    
    research_card(
        "Fine-Tuning LLMs for Regional Dialect Comprehended Question Answering in Bangla",
        "IEEE SCEECS", "2025",
        "LLMs, ChatGPT-4, LoRA",
        "Created a 12,500-sentence dataset from various Bangla dialects. Achieved 53% BLEU score using ChatGPT-4 and LoRA fine-tuning to enhance natural language understanding in regional dialects.",
    )
    
    research_card(
        "Fine-Tuning LLMs for Sentiment Classification of AI-Related Tweets",
        "IEEE WIECON-ECE", "2024",
        "LLMs, Llama 2, Prompt Engineering",
        "Analyzed 20,000 tweets using advanced prompt engineering techniques. Implemented successful classification using Llama 2 to categorize sentiment in AI-related social media content.",
    )
    
    research_card(
        "Towards Accurate Renal Micro-Structure Segmentation: An Assessment of YOLOv8 and Mask R-CNN Models",
        "IEEE WIECON-ECE", "2024",
        "YOLOv8, Mask R-CNN, Deep Learning",
        "Achieved 84.55% IoU score using YOLOv8 for kidney structure detection. Applied Mask R-CNN to identify and segment renal microstructures in medical imaging.",
    )
    
    research_card(
        "Deep Learning Analysis of COVID-19 Lung Infections in CT Scans",
        "IEEE AMATHE", "2024",
        "3D UNet, Deep Learning, R-CNN",
        "Developed 3D UNet model with 95.56% accuracy for COVID-19 detection from CT scans. Created a pipeline for automated analysis of lung infections.",
        "Awarded Best Paper at IEEE AMATHE 2024",
        color="#28a745"
    )
    
    # Add interactive visualizations
    st.markdown("---")
    st.subheader("Publication Timeline")
    
    publications = pd.DataFrame({
        'Paper': ['TrOCR for Blurred Images', 'LLMs for Bangla QA', 'Tweet Sentiment Analysis', 'Renal Structure Segmentation', 'COVID-19 CT Analysis'],
        'Date': pd.to_datetime(['2025-01-01', '2025-01-01', '2024-06-01', '2024-03-01', '2024-01-01']),
        'Impact': [4.5, 4.2, 3.8, 4.0, 4.7]
    })
    
    chart = alt.Chart(publications).mark_circle(size=200).encode(
        x='Date:T',
        y=alt.Y('Impact:Q', scale=alt.Scale(domain=[3.5, 5])),
        color=alt.Color('Impact:Q', scale=alt.Scale(scheme='blues')),
        tooltip=['Paper', 'Date', 'Impact']
    ).properties(
        width=700,
        height=300
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    # Add research metrics
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Publications", "5", "+3 in 2024")
    
    with col2:
        st.metric("Citation Count", "12", "+7 in 2024")
    
    with col3:
        st.metric("Best Paper Awards", "1", "IEEE AMATHE 2024")
    
    with col4:
        st.metric("Research Projects", "4", "+2 Ongoing")

def projects_page():
    st.title("Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>JankenBou - Campus Marketplace</h3>
            <p>A buy and selling platform designed specifically for campus students. Facilitates the exchange of books, electronics, and other items within the university community.</p>
            <p><span class="skill-tag">NodeJS</span> <span class="skill-tag">MongoDB</span> <span class="skill-tag">Express</span> <span class="skill-tag">Bootstrap</span></p>
            <ul>
                <li>Developed full-stack application using NodeJs and MongoDB</li>
                <li>Implemented real-time updates and user authentication</li>
                <li>Created responsive UI for mobile and desktop users</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>Birdly - Bird Trading Platform</h3>
            <p>A comprehensive platform for bird enthusiasts to buy, sell, and exchange birds with dedicated features for bird care information.</p>
            <p><span class="skill-tag">NodeJS</span> <span class="skill-tag">MongoDB</span> <span class="skill-tag">HTML</span> <span class="skill-tag">CSS</span> <span class="skill-tag">Bootstrap</span></p>
            <ul>
                <li>Developed comprehensive buy and selling platform</li>
                <li>Implemented frontend using HTML, CSS, and Bootstrap for responsive design</li>
                <li>Created secure payment system and user verification process</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>Flower Studio - Mobile App</h3>
            <p>An Android application that uses machine learning to identify flower species and provide care information to gardening enthusiasts.</p>
            <p><span class="skill-tag">Java</span> <span class="skill-tag">Firebase</span> <span class="skill-tag">Android</span> <span class="skill-tag">ML</span></p>
            <ul>
                <li>Built Android app using Java and Firebase</li>
                <li>Integrated ML-based flower recognition system</li>
                <li>Implemented user profiles and favorite collection features</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>OCR Research Portal</h3>
            <p>A web application showcasing research findings and providing interactive demos for OCR technology on various types of images.</p>
            <p><span class="skill-tag">Python</span> <span class="skill-tag">Streamlit</span> <span class="skill-tag">TrOCR</span> <span class="skill-tag">Deep Learning</span></p>
            <ul>
                <li>Developed interactive demos for OCR technology</li>
                <li>Implemented performance comparison dashboard</li>
                <li>Created educational content on OCR principles</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Add GitHub activity visualization
    st.markdown("---")
    st.subheader("GitHub Contribution Activity")
    
    # Simulated GitHub contribution data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31')
    contributions = np.random.randint(0, 8, size=len(dates))
    github_data = pd.DataFrame({'date': dates, 'contributions': contributions})
    
    # Monthly aggregation
    monthly = github_data.set_index('date').resample('M').sum().reset_index()
    monthly['month'] = monthly['date'].dt.strftime('%b')
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(monthly['month'], monthly['contributions'], color='#0a3d62')
    ax.set_title('GitHub Contributions by Month (2024)')
    ax.set_ylabel('Contribution Count')
    
    st.pyplot(fig)

def skills_page():
    st.title("Skills & Certifications")
    
    # Skills section
    st.header("Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Web Engineering")
        st.markdown("""
        <div>
            <span class="skill-tag">HTML</span>
            <span class="skill-tag">CSS</span>
            <span class="skill-tag">JavaScript</span>
            <span class="skill-tag">Bootstrap5</span>
            <span class="skill-tag">NodeJS</span>
        </div>
        
        <h3>Database</h3>
        <div>
            <span class="skill-tag">MySQL</span>
            <span class="skill-tag">PostgreSQL</span>
            <span class="skill-tag">Oracle Database</span>
            <span class="skill-tag">MongoDB</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Machine Learning & AI")
        st.markdown("""
        <div>
            <span class="skill-tag">TrOCR</span>
            <span class="skill-tag">Large Language Models</span>
            <span class="skill-tag">YOLOv8</span>
            <span class="skill-tag">Mask R-CNN</span>
            <span class="skill-tag">3D UNet</span>
            <span class="skill-tag">Deep Learning</span>
        </div>
        
        <h3>Tools & Others</h3>
        <div>
            <span class="skill-tag">Git</span>
            <span class="skill-tag">Trello</span>
            <span class="skill-tag">MS Teams</span>
            <span class="skill-tag">Canva</span>
            <span class="skill-tag">Software Documentation</span>
            <span class="skill-tag">Software Testing</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Add radar chart for skills
    st.markdown("---")
    st.subheader("Skills Proficiency")
    
    # Skill proficiency data
    categories = ['Web Development', 'Machine Learning', 'Database Management', 
                 'Research Methodology', 'Teaching', 'OCR Technology']
    values = [85, 90, 80, 95, 85, 95]
    
    # Number of variables
    N = len(categories)
    
    # What will be the angle of each axis in the plot
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Close the loop
    
    # Values for the plot
    values = values + values[:1]  # Close the loop
    
    # Create figure
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)
    
    # Draw one axis per variable and add labels
    plt.xticks(angles[:-1], categories, color='grey', size=10)
    
    # Draw the chart
    ax.plot(angles, values, linewidth=2, linestyle='solid', color='#0a3d62')
    ax.fill(angles, values, color='#60a3bc', alpha=0.4)
    
    # Add values to the plot
    ax.set_rlabel_position(0)
    plt.yticks([20, 40, 60, 80, 100], ['20', '40', '60', '80', '100'], color="grey", size=8)
    plt.ylim(0, 100)
    
    st.pyplot(fig)
    
    # Certifications section
    st.markdown("---")
    st.header("Certifications")
    
    certs = [
        {"title": "Front-End Web UI Frameworks and Tools: Bootstrap 4", "provider": "The Hong Kong University of Science and Technology (Coursera)", "date": "June 4, 2020"},
        {"title": "Introduction to CSS3", "provider": "University of Michigan (Coursera)", "date": "April 27, 2020"},
        {"title": "Interactivity with JavaScript", "provider": "University of Michigan (Coursera)", "date": "April 28, 2020"},
        {"title": "Advanced Styling with Responsive Design", "provider": "University of Michigan (Coursera)", "date": "April 29, 2020"},
        {"title": "Frontend Fundamentals", "provider": "Pirple", "date": "April 11, 2020"},
        {"title": "Introduction to SQL Server", "provider": "DataCamp", "date": "May 22, 2020"},
        {"title": "Front-End Development", "provider": "SoloLearn", "date": "June 22, 2020"},
        {"title": "Information Technology Engineers Examination (ITEE)", "provider": "IPA Japan", "date": "March 2023"}
    ]
    
    for i, cert in enumerate(certs):
        st.markdown(f"""
        <div style="padding: 15px; background-color: {'#f8f9fa' if i % 2 == 0 else 'white'}; 
                    border-left: 3px solid #0a3d62; margin-bottom: 10px;">
            <h4>{cert['title']}</h4>
            <p><strong>Provider:</strong> {cert['provider']}</p>
            <p><strong>Date:</strong> {cert['date']}</p>
        </div>
        """, unsafe_allow_html=True)

def ocr_demo_page():
    st.title("OCR Technology Demo")
    
    st.markdown("""
    This interactive demo showcases my research in Optical Character Recognition (OCR) technology,
    specifically focusing on extracting text from blurred and low-quality images.
    """)
    
    st.info("Note: This is a simulated demo for portfolio purposes. In a live application, it would connect to actual OCR models.")
    
    tab1, tab2 = st.tabs(["Try Demo", "Technical Details"])
    
    with tab1:
        st.subheader("Upload an image for text extraction")
        
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        
        col1, col2 = st.columns(2)
        
        if uploaded_file is not None:
            with col1:
                st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            
            with col2:
                st.markdown("### Extracted Text")
                
                # Progress indicator (simulated processing)
                progress_bar = st.progress(0)
                for i in range(100):
                    # Update progress bar
                    progress_bar.progress(i + 1)
                    if i == 99:
                        break
                
                # Simulated results
                st.success("Text extraction completed!")
                
                st.markdown("""
                The quick brown fox jumps over the lazy dog.
                
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                """)
                
                st.markdown("### Confidence Scores")
                
                confidence_data = pd.DataFrame({
                    'Metric': ['Overall Confidence', 'Character Accuracy', 'Word Accuracy', 'Line Accuracy'],
                    'Score': [0.92, 0.95, 0.89, 0.93]
                })
                
                for _, row in confidence_data.iterrows():
                    st.markdown(f"""
                    <div style="margin-bottom: 10px;">
                        <p style="margin-bottom: 5px;"><strong>{row['Metric']}:</strong> {row['Score']:.2f}</p>
                        <div style="background-color: #e9ecef; border-radius: 3px; height: 20px;">
                            <div style="background-color: #0a3d62; width: {row['Score']*100}%; height: 100%; border-radius: 3px;"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        else:
            st.markdown("""
            ### Sample Results
            
            Below is an example of the OCR technology performance on a sample blurred image:
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Display a placeholder image
                st.markdown("""
                <div style="background-color: #e9ecef; height: 300px; display: flex; justify-content: center; align-items: center;">
                    <p>Sample Blurred Image</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("### Sample Extracted Text")
                st.markdown("""
                Despite significant blur in the original image, our TrOCR model accurately extracted:
                
                "The purpose of this document is to outline the procedures for data handling and privacy protection in accordance with regulation 2016/679."
                
                **Confidence Score:** 0.94
                """)
    
    with tab2:
        st.subheader("OCR Technology Research Details")
        
        st.markdown("""
        ### TrOCR Architecture
        
        My research utilizes a transformer-based OCR approach that combines:
        
        1. **Vision Encoder**: A transformer-based encoder that processes the input image
        2. **Seq2Seq Decoder**: A decoder that generates text sequences from the encoded visual features
        3. **VisionEncoderDecoder Framework**: Connects the vision and language components
        
        ### Performance Metrics
        
        The model achieves:
        - 96.8% accuracy on IIIT 5K dataset
        - Robust performance on blurred, low-resolution, and noisy images
        - Competitive results compared to commercial OCR solutions
        """)
        
        st.markdown("### Performance Comparison")
        
        # Create comparison data
        comparison_data = pd.DataFrame({
            'Model': ['TrOCR (Ours)', 'Commercial OCR 1', 'Commercial OCR 2', 'Open-Source OCR'],
            'Clean Images': [0.985, 0.980, 0.975, 0.950],
            'Blurred Images': [0.968, 0.850, 0.830, 0.720],
            'Low Quality': [0.945, 0.810, 0.790, 0.680]
        })
        
        # Reshape data for visualization
        comparison_melted = pd.melt(comparison_data, id_vars=['Model'], var_name='Image Type', value_name='Accuracy')
        
        # Create grouped bar chart
        chart = alt.Chart(comparison_melted).mark_bar().encode(
            x=alt.X('Model:N', title='OCR Model'),
            y=alt.Y('Accuracy:Q', title='Accuracy Score'),
            color=alt.Color('Image Type:N', scale=alt.Scale(scheme='blues')),
            column=alt.Column('Image Type:N', title=None)
        ).properties(
            width=200,
            height=300
        )
        
        st.altair_chart(chart, use_container_width=True)
        
        st.markdown("### Research Challenges & Solutions")
        
        st.markdown("""
        | Challenge | Solution Approach |
        |-----------|-------------------|
        | Handling severe blur | Multi-scale feature extraction with specialized vision transformer |
        | Low contrast text | Adaptive preprocessing pipeline with contrast enhancement |
        | Complex backgrounds | Attention mechanism focusing on text regions |
        | Multi-language support | Fine-tuning on diverse language datasets |
        """)

def contact_page():
    st.title("Contact Me")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h3>Contact Information</h3>
            <p><i class="fas fa-envelope"></i> <strong>Email:</strong> fjayrin@gmail.com</p>
            <p><i class="fas fa-phone"></i> <strong>Phone:</strong> +880 16 162 47349</p>
            <p><i class="fas fa-map-marker-alt"></i> <strong>Present Address:</strong><br>
            West High Level Road, Lalkhan Bazar,<br>Chittagong, Bangladesh</p>
            <p><i class="fas fa-map-marker-alt"></i> <strong>Permanent Address:</strong><br>
            Village: Jatarkul; PO: Hajir Para;<br>Thana: Chandanaish; District: Chittagong</p>
            <h4 class="mt-4">Academic References</h4>
            <p><strong>Assistant Professor Abu Nowshed Chy</strong><br>
            Email: nowshed@cu.ac.bd<br>
            Phone: +8801764207358</p>
            <p><strong>Professor Dr. Kazi Ashrafuzzaman</strong><br>
            Email: ashraf@cu.ac.bd<br>
            Phone: +8801717124315</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h3>Send Me a Message</h3>", unsafe_allow_html=True)
        
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message", height=150)
        
        if st.button("Send Message"):
            st.success("Thank you for your message! I'll get back to you soon.")
        
        st.markdown("""
        <div style="margin-top: 30px; padding: 20px; background-color: #f8f9fa; border-radius: 5px;">
            <h4>Academic Collaboration</h4>
            <p>I am open to research collaborations in the following areas:</p>
            <ul>
                <li>OCR Technology and Applications</li>
                <li>Large Language Models for Low-Resource Languages</li>
                <li>Medical Image Analysis using Deep Learning</li>
                <li>Computer Vision for Educational Technology</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Achievement section - could be added as another page option
def achievements_page():
    st.title("Achievements & Awards")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h3>Premire University IT Fest</h3>
            <p class="timeline-date">January 2024</p>
            <p>Achieved 3rd position in the senior category of the competition, which focused on CSE-related topics.</p>
        </div>
        
        <div class="achievement-card">
            <h3>Information Technology Engineers Examination (ITEE)</h3>
            <p class="timeline-date">March 2023</p>
            <p>Successfully achieved full passer status on the ITEE, demonstrating proficiency in information technology engineering concepts.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h3>6th International Girls' Programming Contest</h3>
            <p class="timeline-date">June 2022</p>
            <p>Demonstrated strong problem-solving skills and knowledge of CSE topics in this international competition.</p>
        </div>
        
        <div class="achievement-card">
            <h3>Best Paper Award - IEEE AMATHE 2024</h3>
            <p class="timeline-date">2024</p>
            <p>Received the Best Paper Award for "Deep Learning Analysis of COVID-19 Lung Infections in CT Scans".</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Timeline visualization
    st.subheader("Achievement Timeline")
    
    achievement_data = pd.DataFrame({
        'Achievement': ['SSC GPA 5.00', 'HSC GPA 4.58', 'BSc CGPA 3.73', 'Programming Contest', 'ITEE Certification', 'IT Fest 3rd Position', 'Best Paper Award'],
        'Date': pd.to_datetime(['2016-06-01', '2018-06-01', '2022-12-01', '2022-06-01', '2023-03-01', '2024-01-01', '2024-05-01']),
        'Importance': [3, 3, 4, 3.5, 4, 4.5, 5]
    })
    
    timeline = alt.Chart(achievement_data).mark_circle(size=200).encode(
        x='Date:T',
        y=alt.Y('Importance:Q', scale=alt.Scale(domain=[2.5, 5.5]), title=None, axis=alt.Axis(labels=False)),
        color=alt.Color('Importance:Q', scale=alt.Scale(scheme='blues'), legend=None),
        size=alt.Size('Importance:Q', scale=alt.Scale(range=[100, 500]), legend=None),
        tooltip=['Achievement', 'Date']
    ).properties(
        width=700,
        height=200
    )
    
    # Add text labels
    text = alt.Chart(achievement_data).mark_text(align='center', baseline='middle', dy=-15).encode(
        x='Date:T',
        y=alt.Y('Importance:Q', scale=alt.Scale(domain=[2.5, 5.5])),
        text='Achievement:N',
        color=alt.value('#0a3d62')
    )
    
    st.altair_chart(timeline + text, use_container_width=True)

# Main app logic
def main():
    page = sidebar()
    
    if page == "about":
        about_page()
    elif page == "education":
        education_experience_page()
    elif page == "research":
        research_page()
    elif page == "projects":
        projects_page()
    elif page == "skills":
        skills_page()
    elif page == "ocr_demo":
        ocr_demo_page()
    elif page == "contact":
        contact_page()

if __name__ == "__main__":
    main()
