# Digital Twin Approach for Operation and Maintenance of Transportation System—Systematic Review - PMC

Sumber file: raw_PMC11435829_Digital_Twin_OM_Transportation_Review.html
Diunduh: 2026-09-12 (arsip teks otomatis)

---

Digital Twin Approach for Operation and Maintenance of Transportation System—Systematic Review

Faculty of Mechanical Engineering, Wroclaw University of Science and Technology, Wyspianskiego 27, 50-370 Wroclaw, Poland; robert.giel@pwr.edu.pl (R.G.); klaudia.winiarska@pwr.edu.pl (K.W.)

Received 2024 Aug 2; Revised 2024 Aug 30; Accepted 2024 Aug 31; Collection date 2024 Sep.

Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (

https://creativecommons.org/licenses/by/4.0/

There is a growing need to implement modern technologies, such as digital twinning, to improve the efficiency of transport fleet maintenance processes and maintain company operational capacity at the required level. A comprehensive review of the existing literature is conducted to address this, offering an up-to-date analysis of relevant content in this field. The methodology employed is a systematic literature review using the Primo multi-search tool, adhering to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines. The selection criteria focused on English studies published between 2012 and 2024, resulting in 201 highly relevant papers. These papers were categorized into seven groups: (a) air transportation, (b) railway transportation, (c) land transportation (road), (d) in-house logistics, (e) water and intermodal transportation, (f) supply chain operation, and (g) other applications. A notable strength of this study is its use of diverse scientific databases facilitated by the multi-search tool. Additionally, a bibliometric analysis was performed, revealing the evolution of DT applications over the past decade and identifying key areas such as predictive maintenance, condition monitoring, and decision-making processes. This study highlights the varied levels of adoption across different transport sectors and underscores promising areas for future development, particularly in underrepresented domains like supply chains and water transport. Additionally, this paper identifies significant research gaps, including integration challenges, real-time data processing, and standardization needs. Future research directions are proposed, focusing on enhancing predictive diagnostics, automating maintenance processes, and optimizing inventory management. This study also outlines a framework for DT in transportation systems, detailing key components and functionalities essential for effective maintenance management. The findings provide a roadmap for future innovations and improvements in DT applications within the transportation industry. This study ends with conclusions and future research directions.

digital twin, operation and maintenance, transportation system, systematic review analysis, air transportation, railway transportation, land transportation, in-house logistics, water and intermodal transportation, supply chains operation, PRISMA guidelines

The dynamics of the transportation market and the growing demands of customers pose significant challenges for transportation companies in the context of maintaining the durability and reliability of transport means. The transportation industry is subject to continuous changes resulting from various factors, such as technological advancements, changing regulations, and consumer trends. In recent years, the dynamic development of the transportation sector can be observed as driven by ongoing globalization, the growth of international trade, and increasing societal mobility. Transportation companies face intensified competition from both traditional and new, innovative entities. Market dynamics force them to constantly adapt to changing conditions and seek new solutions and technologies to maintain a competitive position [

Simultaneously, the growing demands of customers on transportation companies are becoming increasingly diverse. Customers expect quick and timely delivery of goods and high-quality service, safety, and flexibility in adapting services to individual needs. High customer demands require transportation companies to ensure the efficient operation of their fleets and the quality of services provided at every stage of the transportation process. This entails implementing fast and efficient customer service procedures and having a modern vehicle fleet with effective maintenance management and quick emergency response. In this context, ensuring the high maintainability and reliability of the transportation fleet becomes a key issue [

The challenges related to maintaining high maintainability and reliability of the transportation fleet are significant for companies operating in the transportation sector due to the dynamic nature of the transportation environment and the variety of factors affecting vehicle performance. One of the main issues associated with maintaining the transportation fleet’s reliability is the vehicle fleet’s aging. Transport vehicles are operated under various weather and road conditions, leading to natural wear and degradation of mechanical parts and electronic components. Over time, the risk of failures and downtimes increases, negatively impacting the operational efficiency of transportation companies [

Another significant issue is the complexity of maintenance processes for the vehicle fleet. Regular technical inspections and repairs are required to ensure operational readiness and the necessary level of vehicle safety. Managing these maintenance processes is often demanding and time-consuming, especially when providing the proper maintenance level for large transportation fleets operating on diverse routes and under various operational conditions [

Additionally, the necessity for a quick response in case of failures and unforeseen situations is also problematic. Vehicle downtimes can lead to delivery delays, generating costs and negatively impacting the company’s reputation. Therefore, transportation companies must take appropriate measures to minimize the risk of failures and downtimes and ensure the operational continuity of their fleets. Implementing modern methods and technologies, such as digital twins (DTs), can improve the efficiency of fleet maintenance processes and maintain the company’s operational capabilities at the required level. Investments in modern technological solutions allow for improved fleet durability and reliability, minimized operational costs, and increased market competitiveness.

Recently, numerous studies and publications have emerged in the transportation sector, focusing on maintenance management and modeling to enhance the efficiency of maintenance processes (for a comprehensive review, see, for example, refs. [

]). The search for English language review publications in the Scopus database based on searching the following keywords—“

maintenance OR maintenance management OR condition monitoring OR predictive maintenance

”—allowed for 24 relevant records to be identified. The identified papers were published from 2010 to 2024. The content analysis of these reviews revealed that most of these reviews are focused on specific transport sectors—railway maintenance [

], electric vehicles and fuel cell condition monitoring [

]. In addition, a few reviews are focused on transportation infrastructure maintenance [

]. However, there is a notable absence of comprehensive review articles addressing the application of digital twins in transportation system operation and maintenance especially in the context of in-house logistics systems. Despite the growing interest in digital twin technology and its potential benefits for the transportation sector, the current literature lacks thorough reviews that summarize existing knowledge and identify research gaps in this specific area. Only two of the identified reviews focus on the aspect of DT use in the maintenance of transportation systems. First, the authors in [

] concentrate on the integration of Digital Twins and their impact on the evolution of transportation asset management systems. Secondly, Selvam et al. [

] provide an in-depth analysis of the current advancements in incorporating digital twins into the maintenance of integrated chargers in electric vehicles.

This study provides a comprehensive overview of academic research on the application of digital twins in the operation and maintenance of transportation systems, with special emphasis on internal transportation. The primary goal is to identify key research trends in this field and suggest potential future research directions. Additionally, based on the literature review, a framework for digital twins in the internal transport sector is developed, drawing from the physical asset management concept and ISO/DIS 23247 standards [

]. Consequently, this paper contributes to the existing knowledge on digital twins in transportation systems in three ways: (1) identifying the major research trends related to DT applications in the operation and maintenance of transportation systems, with a focus on in-house logistics; (2) outlining future research directions for the study of DT in transportation systems operation and maintenance; and (3) developing a framework for DT in transportation system maintenance management.

Based on these objectives, the research questions are as follows:

RQ1: What is the state of the literature on digital twin use in transportation systems operation and maintenance between 2012 and 2024?

RQ2: What are the main research and knowledge gaps in DT use in transportation systems operation and maintenance, especially in the context of in-house logistics?

RQ3: Which aspects of DT modeling require further advancement to address future challenges in transportation systems?

RQ4: What scope should the framework for digital twin for maintenance management of transportation systems have?

This paper addresses the research questions posed above by employing bibliometric performance analysis and systematic analysis using the PRISMA method (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) [

]. This approach is designed to summarize and pinpoint the key research areas within the identified application fields.

In summary, the article is structured into seven sections. Following the Introduction (

) outlines the concept of digital twins and explores their application across various transportation sectors. The Review Methodology (

) details the primary methods used for the review, including the strategy for the literature search and the criteria used to assess the relevance of the analyzed documents.

presents the main findings of the systematic literature review for the selected papers within the seven identified application fields.

then discusses the results related to these application fields, identifying gaps in the literature and knowledge.

introduces a newly developed DT framework for the maintenance of transportation systems. The final section, Conclusions (

), provides a summary of contributions, outlines limitations, and offers recommendations for future research.

Digital twin (DT) is one of the key Industry 4.0 technologies. Although DT has gained a lot of interest in many sectors in the last five years, the first proposals for the concept were made in 1991. The history of the origin and evolution of technology to its current form can be read in [

The DT concept is relatively new; no coherent definition has yet been created. At the same time, it is constantly evolving due to technological advances, industry needs, and user needs, so the possibilities for its use have changed over the past few years [

]. The definitions presented in the literature and the essence of the concept are often related to the area in which it is applied [

]. Among others, examples of implementing the DT concept in practice can be found in [

]. Most publications on the areas of DT implementation are related to production systems. However, the concept is also increasingly appearing in agriculture and medicine. In addition, DT also finds applications in psychology [

In this paper, the authors focused on transport and logistics issues. In this context, the definitions often used in the literature target the specific transport branches for which the DT solution is developed. Therefore, it can be seen that some of the definitions tend to contradict each other. Hence, based on a thorough analysis of the definitions provided by D. Jones [

] for this work, it is assumed that a digital twin (DT) is a virtual representation of the actual process/asset/system based on Industry 4.0 technology use, where such activities as data sharing, simulation, time-based monitoring, data analysis, testing, and optimization are included. The combination of these technologies and activities aims at real-time monitoring, control, prediction, optimization, and more informed and faster operational decision-making [

The digital twin of any object in its basic version is built from three basic elements: a physical object (resource/asset), a virtual representation of the object (model), and the connection between them [

]. The represented object can be a product, process, or system. A DT is a virtual representation of any real object that encompasses all its features [

]. In addition, data are automatically shared in real time between the physical object and the digital counterpart [

]. This factor distinguishes a digital twin from a digital model (DM) or digital shadow (DS). This means that a DT is dynamic. In a DM, the interaction between the real object and its digital copy is manual. It is merely a virtual representation of the real object. In addition, the DM does not process input data and cannot react to changes in the real object [

]. In the case of a DS, the data transfer from the real object to the digital object is automatic, while the feedback is already manual. This allows for an accurate virtual representation of the real processes; however, the feedback is not provided automatically [

graphically illustrates the data flow in the concepts discussed. In the literature, the DM is seen as part of the DT, which enables the virtual visualization of the real object, and the DS is referred to as a digital design aiming at a DT, but it does not meet all the assumptions of a DT [

Data flow in different modes of integration. Source: own contribution based on [

The improvement of the DT concept and the success of its implementation is made possible by the rapid development of other Industry 4.0 technologies on which DT is based, i.e., IoT, big data, or machine learning [

]. The data that DT uses comes from the real-world object, the model, and information about historical operations. Data from the real-world object are obtained using various sensors that provide real-time information. Additionally, through the use of IoT, which enables data collection and transmission, as well as data sharing, DT can collect information about different objects and their models [

]. The real-time transmission of data allows for the DT to be updated in real-time so that it does not deviate from the real object and accurately reflects its performance level or, e.g., degradation level [

]. By constantly transmitting a large quantity of new data from different sources, it is possible to maintain the dynamic nature of the DT. This provides the possibility to monitor the object and to accurately reflect it digitally in real-time. With the diversity of data sources, access to big data is necessary. All the collected data are analyzed through machine learning, and a dynamically changing virtual model is created based on this. The next step is to generate conditions that have not yet occurred in reality. The behavior of the object operating under the given conditions is also studied. In addition, problems that may arise under the given operating conditions are predicted [

]. This makes it possible to detect and eliminate errors in the virtual system before they occur in the real process [

]. Finally, some solutions are proposed to minimize the possibility of failure occurrence and completely prevent the identified problems [

]. Thanks to the bidirectional automatic connection between the physical and the digital object, information from simulations and predictions is transferred to the physical object, which is used in the operational process [

The processes discussed above are the basic scope of DT functionality. These activities can also take place using machine learning algorithms [

illustrates the concept of DT operation. In addition, the accuracy and usability of DT are highly dependent on the quality of the sensor data provided by the real object [

]. Poor accuracy of this data or sensor failures cause interference with real-time monitoring of the object. Additionally, they can even lead to the failure of the physical object as it is operated based on feedback from the DT [

The digital twin operation concept. Source: own contribution based on [

At the same time, an important aspect in the context of DT definition and development is the reference to the product lifecycle. Identifying the phases of DT development in relation to the product lifecycle allows for a clear definition of the basic tasks of DT in an organization. In addition, a DT may accompany its real-life twin from the early stages of its development, so it is beneficial to distinguish the phases of DT development throughout the object’s lifecycle.

DT is applicable throughout the whole lifecycle of a physical object, from the design phase through the production and operation phases to its disposal [

], the authors presented different stages of DT maturity. Based on their research results, the DT lifecycle was developed, which coincides with the lifecycle of the real object (

Digital twin lifecycle in relation to the lifecycle of an object. Source: own contribution based on [

The first phase of the DT lifecycle is the digital twin prototype (DTP). It is designed for the object design activities. At this phase, the real object does not yet exist in its physical form. It only exists as a concept and design in virtual space, such as DTP [

]. Based on the information from the DTP, a physical object is developed that duplicates the digital version. In [

], DT types that partly overlap with the DTP assumptions are proposed. However, due to their purpose, they can be said to be only part of DTP. Early-stage digital twin (ESDT) corresponds to a real object’s conception and design phase. It aims to generate information and evaluate proposed solutions and concepts. This is possible through early simulation and analysis [

]. Experimentable digital twin (EDT) corresponds to the research and development phase of the lifecycle of a real object. An EDT is a virtual prototype intended primarily to test and verify a designed object or system in its target operational environment [

The DT maturity stage corresponding to the exploitation and disposal phase of the real object is the digital twin instance (DTI). The DTI represents a concrete physical object and evolves throughout its lifetime until disposal. It contains past, current, and projected operational data and service records [

The concept of DT has been gaining particular interest over the last five years, whether in terms of the development of the approach itself, the building of customized architectural solutions, DT characteristics, design principles, or future challenges. As a result, a number of articles can be distinguished that aim to summarize the basic literature on DT designing, modeling, and implementation. For example, a comparison of different definitions describing DT is presented in [

], the architecture and modeling approach are described in [

], and the link between Industry 4.0 development and DT is described in [

]. In contrast, DT in Industry 5.0 is investigated in [

]. The main challenges are reviewed, e.g., in [

]. A summary of recent review papers that focus on DT concept definition, modeling, architecture, or research challenges is given in

A summary of recent papers focused on providing an overview of the literature in the area of the digital twin concept.

Analysis of the state-of-the-art definitions of DT, investigation of the main characteristics of DT, and exploration of DT applications

Survey of the state-of-the-art of major definitions, specifications, and implementations of the DT concept in several technological areas with an attempt to consolidate the major features of the DT concept as it has emerged in different industries

Review of digital twinning, particularly focusing on the role of AI-ML and big data

IEEE Xplore, ACM digital library, Scopus (ScienceDirect, Elsevier), SpringerLink, Hindawi, IGI-Global, Taylor & Francis Online, Wiley online library, the US patents database

Review the evolution of DTs in tomorrow’s digital factories and research toward implementing context-aware, autonomous, and adaptive DTs.

Review of DT history, definitions, models, types of key enabling technologies, and applications

Review of existing reviews relating to DT

AISeL, IEEE Xplorer, Science Direct, Springer Link

Review of various DT features and current approaches, the shortcomings and reasons behind the delay in the implementation and adoption of digital twin and development of DT reference model

A comprehensive view of the DT technology and its implementation challenges and limits in the most relevant domains and applications in engineering and beyond

ResearchGate, MDPI, Science Direct, and ProQuest

Review of the current state of digital twins, describing the terms digital model and digital shadow; review the concepts of Internet of Things (IoT) and Industry 4.0

Survey of potential threats associated with the DT paradigm, taking into consideration its functionality layers and the operational requirements

Review of research and applications of DT in smart manufacturing

Review of recent advancements in the DT in the context of technology, market potential and trends,

Reviewing of SLRs on DTs and analyzing the body of related work with respect to the presented research scope

Review of digital twin definition, emphasizing important characteristics; analysis of techniques, trends, and future research directions

Systematic review according to Kitchenham’s guidelines [

Literature review on Digital Twins in the context of intelligent automation use in different industries

Review on data management solutions proposed in the DT context

ACM Digital Library, IEEE Digital Library, Onepetro, Scopus, Science Direct, Web of Science database

2.2. Digital Twin Concept—Implementation Areas

As has already been mentioned, DT is currently being implemented in various industrial sectors due to its broad applicability. As an innovative approach, it provides new solutions to problems faced by numerous industries, ranging from designing new products or even factories to issues related to optimizing the operation of selected technical systems or organizations. Due to such a high level of interest in the possibilities of DT implementation, we can currently distinguish a number of works summarizing recent developments in this area (see, e.g., refs. [

]). At the same time, based on the literature analysis carried out, it was possible to propose basic areas of DT practical application (

The digital twin concept’s main implementation areas. Source: own contribution.

Digital twin technology, which creates detailed and dynamic virtual replicas of physical systems, is revolutionizing numerous industries by providing real-time insights and predictive capabilities. As shown in

, this technology is being implemented across a wide range of sectors, enhancing efficiency, performance, and innovation in diverse applications.

Digital twins are increasingly applied across various industries to enhance operations and efficiency. In aviation, they monitor aircraft conditions, predict maintenance needs, and optimize operations, improving safety and reliability [

]. In smart manufacturing, digital twins enable real-time insights, predictive maintenance, and workflow optimization, integrating IoT, AI, and machine learning for greater productivity and flexibility [

]. The automotive industry benefits from digital twins in vehicle design, manufacturing, and maintenance, supporting innovations in electric vehicles and autonomous driving [

]. In the mining industry, digital twins improve safety, resource management, and operational efficiency [

]. In logistics and transportation, they optimize routes, fleet management, and predictive maintenance [

]. Additionally, digital twins enhance supply chain management by providing real-time tracking and improving demand forecasting [

]. Other applications include robotics, where they are used for simulation, testing, and real-time control of robotic systems [

], and in education, training, healthcare, and psychology, where they offer immersive learning experiences and personalized treatments (see, e.g., refs. [

In addition, due to the introduction of the DT lifecycle given in

, it is worth investigating how the implementation areas are aligned with the phases of the lifecycle of an object. DTs provide invaluable insights and optimizations throughout the object’s lifecycle—design, production, operation, and end-of-life. DTs allow for virtual prototyping and testing in the design phase, reducing time and costs. During production, they enable real-time monitoring and quality control, enhancing efficiency. DTs facilitate predictive maintenance and performance optimization in the operational phase, extending product lifespan. Finally, at the end-of-life phase, DTs assist in planning for recycling or disposal. This comprehensive integration across the product lifecycle highlights the transformative potential of digital twins.

shows for which purposes DT was applied during the different phases of the object’s lifecycle.

The digital twin concept’s main implementation areas in relation to the object’s lifecycle. Source: own contribution based on [

From the point of view of this article, which focuses on maintenance issues, the third phase of the object’s lifecycle is of most interest.

With increasing frequency, authors describe the possibility of using DT in maintenance operations and management. In the context of maintenance, DT plays an important role because it offers the possibility to evolve the way maintenance is carried out. This means the possibility of moving towards more advanced maintenance strategies such as predictive or prescriptive maintenance [

]. Preventive maintenance without the use of DT is only used as a calculation tool to analyze the condition of an object and predict faults [

]. The results then obtained do not reflect the long-term dynamically changing real-world data. DT provides more intelligent maintenance management than in the case of predictive maintenance implementation. This is due to the automatic analysis of the collected data related to the operation, technical condition, or facility utilization. Based on this data, it is possible to predict failures, anticipate maintenance, or plan corrective action in response to certain irregularities in real time [

Most of the application cases of DT in maintenance concern optimizing maintenance decisions [

]. The condition of the actual facility is predicted so that an appropriate maintenance plan can be selected. Monitoring the condition of the facility during the operational phase enables DT to plan maintenance more effectively. The differences between traditional and DT-based predictive maintenance are described in [

]. The use of DT in maintenance also contributes to technical systems’ reliability, efficiency, and safety [

The confirmation of increasing interest in DT implementation in the maintenance fields may be the analysis of the number of published papers per year. An initial study was performed based on the data from two databases, Web of Science and Scopus, in July 2024. The search process was based on using two keywords, “digital twin” and “digital twin AND maintenance”, and searching within all fields. The results are presented in

. Analyzing the graph, we may state that since 2018, there has also been an increasing trend in the number of publications that describe the link between DT and maintenance. Comprehensive reviews of digital twin use in maintenance areas, presented in, e.g., refs. [

Publications from 2014–2022 that were published in the Scopus and Web of Science databases and included the term DT and combinations of the terms DT and maintenance. Source: own contribution.

The fundamental nature and wide-ranging applications of digital twin (DT) technology, particularly in maintenance, highlight the necessity of examining its role in the operation and maintenance of transportation systems. The transportation sector encompasses various branches and addresses numerous issues requiring a systematic and organized approach. Therefore, it is essential to evaluate how the current review of digital twin technology, focusing on maintenance, emphasizes its significance in transportation system operations. This examination aims to ensure that the contributions and potential of digital twin technology in enhancing maintenance practices within transportation are appropriately highlighted and understood. Additionally, the objective is to identify the main research trends, knowledge gaps, and future research directions in this field, providing a comprehensive overview to guide further studies and advancements.

2.3. Digital Twin in Transportation Systems

The digital revolution has led to the development of intelligent transport systems technology. This has resulted in the widespread deployment of sensors in transport networks. These sensors provide real-time access to data that can be the basis for communication with a virtual model. This, in turn, enables the use of DTs in transport systems. Indeed, with the large quantity of data collected, DTs can potentially improve the transport sector. As a result, a DT can currently operate, control, or analyze existing/designed transport systems [

A preliminary analysis of the literature shows that, from 2019 onwards, a marked increase in the number of publications can be observed in the context of the design and implementation of the concept of digital twins to ensure the operational continuity of transport systems [

]. In some publications, the term transportation digital twin (TDT) appears. As TDT is in its infancy, it is, therefore, difficult to find a single, universally accepted definition of the concept [

]. As in the general definition of a DT, a TDT can be defined as a digital representation of a transport system’s physical elements that react to real-time changes. Both transport assets and connected services, even those that are not transport-related, are digitally mapped. The term TDT is not yet widely used, and it is most common in the literature to find a description of DT for specific applications of this technology in selected transport systems.

This concept finds application in all branches of transportation. It is currently used in maritime transport for predicting potential failures, optimizing fleets, ports, and terminals, and for comprehensive supply chain optimization [

]. In air transport, DTs can be utilized to control airport transportation systems [

]. The land transport sector is also widely described in the literature. DTs are applied in both long-distance transport (rail and road) and internal transport. In rail transport, authors propose using DTs to monitor railway switches, increase railway network capacity, and general management in the sector [

]. Road transport is another widely discussed application area for DTs, where it is used for optimizing traffic conditions, planning urban transportation, calculating recommended vehicle speeds, controlling traffic signals, visualizing possible scenarios, and enhancing road safety [

]. DT is most commonly proposed in internal transport for planning, optimizing transport processes, and vehicle route planning [

Although transportation infrastructure is gradually adapting to new technologies, the application of digital twins in transportation engineering is currently in its early stages [

]. The main goal of using DT in transportation is to enhance the safety and mobility of transportation systems [

]. The first review articles in this area appeared in 2020 and focused on selected application areas. The first review article on the use of DTs in transportation was published in 2020 by R. Phanden et al. [

]. This article describes the application of DT technology in aviation, robotics, and manufacturing. The authors focused on DT simulations and analyzed eleven aviation-related works, two on robotics and five on manufacturing. This analysis involved presenting how simulations and DT were utilized in each publication.

] pertains to internal transport. The authors presented five main trends that contemporary research on DT in internal transport systems focuses on. A broader analysis included 34 publications. This analysis focused on the use of DT in internal process optimization. It was noted that DTs are mainly built to increase the physical object’s efficiency and respond better when disruptions occur due to random events. The authors in [

] proposed a systematic review of the literature on current applications of DT in railway and road networks. The analysis results indicated that most DT applications in this sector are concerned with operation and maintenance. Another review article is dedicated to the maritime transport sector [

]. The DT of a ship is most often used for maintenance planning, failure prediction, and process optimization on the ship. However, the authors emphasize that real-time communication with the physical object is the biggest challenge in using a ship’s DT. In [

], publications focusing on transport safety and mobility were analyzed. The authors also proposed a concept of DT for transportation systems. Kaiblinger et al. presented the current trends in DT development in production logistics in their publication [

], the authors focused on analyzing the potential applications of DT in electric autonomous vehicles. The analyzed articles concerned battery charging, driver experience, and vehicle monitoring and control.

Again, the confirmation of increasing interest in DT implementation in the transportation sectors may be in analyzing the number of published papers per year. An initial analysis was performed based on the data from two databases, Web of Science and Scopus, in July 2024. The search process was based on using two keywords, “digital twin AND transport” and “digital twin AND transport AND review”, searching within all fields. The results are presented in

. A summary of reviewing articles that focus on DT use in transportation systems is presented in

A number of publications and review articles in Scopus and Web of Science databases between 2019 and 2023 related to digital twins in transport systems. Source: own contribution.

A summary of recent papers focusing on providing a literature overview in the area of the digital twin concept used for transportation systems.

Level of Analysis (System/Process/Object)

Review of simulation-based DT and DT-based simulation models proposed for aerospace, manufacturing, and robotics

Overview of the academic research on the DT applied in internal transport systems of which inherent attributes are flows of materials and accompanying information.

Review of technology, development, and types of digital twins, as well as possibilities of their application in logistics

on DT technology for intelligent transportation systems focusing on the use of DTs in electric mobility and in autonomous vehicles

Definition of the term “digital twin of a ship”; review analysis of developed digital twins for ships

Presentation of the current scope of DT applications in railway and road networks with particular focus on sustainability and resilience

Reviewing of literature on transportation-related DT systems, presenting a reference architecture and framework for TDT systems focused upon safety, mobility, and environmental aspects, and identifying the challenges that arise from the requirements of such TDT systems

Presentation of current DT development trends in production logistics

Study of the application of BIM and DT in the transportation industry

Land transportation (road, rail), air transportation

Examination of the potential of digital twins in urban risk management,

specifically in addressing disaster risks and enhancing resilience in urban environments

In summary, interest in the digital twin concept is steadily growing in relation to transportation systems performance, as confirmed by the data in

. DTs have a wide range of applications in transportation systems across all transport branches (air, maritime, and road transport). This technology is increasingly important in this area, contributing to improved efficiency, safety, and sustainability. On the other hand, the growing customer demands placed on transportation companies are becoming more diverse. Customers expect quick and timely delivery of goods and high-quality service, safety, and flexibility in adapting services to individual needs. High customer demands mean that transportation companies must ensure the efficient operation of their fleets and quality of services provided at every stage of the transportation process. This requires not only the implementation of quick and efficient customer service procedures but also the possession of a modern vehicle fleet with effective maintenance management and quick response in emergencies. These challenges can be addressed using DT, which can be applied to predict failures, anticipate maintenance, and plan repair actions based on real-time data.

Additionally, while previous reviews have explored DT applications within specific transportation sectors or broadly within operational and maintenance contexts, this paper offers a novel contribution by providing a comprehensive synthesis of DT applications across multiple transportation domains with a focused emphasis on in-house logistics. Our review addresses two critical gaps in the current literature:

Lack of comprehensive reviews: Although there is a growing body of work on DTs in various sectors, there is a notable absence of reviews that integrate insights across different transportation branches specifically in the context of operational and maintenance (O&M) practices. Most existing reviews either focus narrowly on specific transportation modes or broadly on DT applications without delving deeply into the unique O&M needs of internal logistics. This paper fills this gap by offering a detailed overview and critical analysis of how DTs can enhance O&M across diverse transportation sectors with particular importance of logistic systems.

Insufficient focus on in-house logistics: The application of DTs in the maintenance of transportation systems, particularly in-house logistics, remains underexplored. Our review emphasizes this aspect, providing a structured framework that highlights how DT can address the unique challenges associated with internal logistics management. This focus on in-house logistics is a distinguishing feature of our work and represents a significant advancement in understanding and applying DT technology in this critical area.

The presented section outlines the main adopted assumptions and steps in the systematic literature review (SLR) adopted in this study. An SLR focuses on identifying, evaluating and interpreting all available research relevant to a particular research question, or topic area, or phenomenon of interest [

]. It is widely accepted that conducting an SLR is a fundamental scientific activity that follows a standard procedure for developing, conducting, and reporting processes [

The main goal of the conducted review is to investigate the main research directions and gaps in digital twin modeling in the context of transportation systems operation and maintenance. The SLR was performed based on the established guidelines proposed by [

]. The basis for reporting systematic review conducted by the research team was the PRISMA guidelines [

]. The SLR process consists of 9 steps across three phases, namely, planning (3 steps), conducting (3 steps), and documenting (3 steps). It is illustrated in

Research framework and methods/tools used for systematic literature review. Source: own contribution.

The next subsections discuss in detail the research work conducted in these three phases.

In this section, the main steps related to the planning of this SLR study are presented. The motivation of this study is to investigate, classify, and synthesize the relevant literature on digital twins in the operation and maintenance of transportation systems based on the thematic overview of the primary studies. As an output of the first step of the planning process, the main objectives of this study are defined. As has been previously stated, they include (a) establishing the body of knowledge of transportation systems operation and maintenance performance in the context of digital twin use by identifying and classifying the extant research on this topic; (b) identifying the main knowledge and research gaps in this research area; and (c) identifying development trends and the opportunities for future research. To achieve these objectives, the main research questions are stated (Step 2):

The definition of the research questions was preceded by an extensive analysis of the issues addressed in the literature in the context of DT modeling, DT use in maintenance, DT use in transportation systems, and DT use in production and industry sectors according to the theory background, presented in

. The identified research gap clearly indicates the need for research to develop a framework for digital twin-based maintenance management of transportation systems in the context of in-house logistics operations. In addition, the defined research questions and preliminary analysis of the available literature provided the possibility to determine the research framework for this study, relevant tools and methods to be used, and the main inclusion and exclusion criteria (Step 3).

The second phase of the performed methodology includes steps 4, 5, and 6, which are discussed in detail below.

3.2.1. Collection of Publications for Review

First, the literature-searching process was carried out. It was based on the use of the multi-search tool Primo [

]. The Primo tool searches a library’s collection of resources based on keywords and uses a range of filters to refine one’s analyses. Based on this, we can create search strategies based on resources from different scientific databases, such as e.g., Scopus, Web of Science, ScienceDirect database, Elsevier, Wiley, and Springer publisher databases. The literature search was conducted between 17 June and 17 July 2024.

The search string covered English search terms used in various combinations applying a Boolean operator, AND and OR. The search query was based on keywords related to digital twin, maintenance-related, and transportation-related aspects. The maintenance-related keywords were identified based on review papers [

], whereas transportation-related keywords were defined according to review papers [

]. In addition, the keyword selection process was designed to encompass both contemporary and historical terms relevant to DT technology in transportation systems operation and maintenance. As a result, we took into account the relevance of keywords to the research scope and historical context. We also applied an initial broad search strategy with a review of related terms (e.g., “cyber-physical systems”, “simulation-based models”, “virtual models”) before the final definition of the keywords.

The final selected keywords were determined to provide the widest possible coverage of the digital twin-based research in the context of operation and maintenance and transportation systems. The final search engine includes the following:

(ALL = (digital twin)) AND (ALL = (maintenance OR maintenance management OR fault OR diagnosis OR prognosis OR condition monitoring OR predict OR diagnostic)) AND (ALL = (transport OR transportation OR robot OR warehouse OR mobile OR railway OR aircraft OR vehicle OR land OR logistic OR forklift OR intermodal OR internal))

Based on the presented criteria, the initial search allowed for the identification of 2509 scientific papers, which were later analyzed in the screening process (

3.2.2. Screening of Collected Publications

The screening process allowed for the identification of papers relevant to full-text analysis. First, the studies were limited to those published between 2012 and 2024 to ensure recent and relevant advancements were included.

To ensure a thorough and accurate evaluation of each study’s relevance to the topic of digital twin (DT) applications in transportation systems’ operation and maintenance, we imposed two key inclusion criteria: full-text availability and publication in English. The availability of full text was crucial for an in-depth assessment of the study’s content and its alignment with our thematic focus. This allowed for us to thoroughly review and evaluate the methodologies, findings, and relevance of each paper. Additionally, English-language publications were selected to facilitate comprehensive understanding and consistent interpretation of the research, ensuring that the studies could be accurately assessed for their contribution to this review’s objectives.

Based on these inclusion criteria, 124 papers were excluded from further analysis.

The screening process had the purpose of filtering out papers that were not related to the main topic. Therefore, a two-step analysis was performed. First, the records were scanned by title and abstract by all authors. Studies were included if their abstracts indicated a focus on DT applications in transportation systems, operation, and maintenance. Later, we compared team members’ opinions at a research team meeting. In case of discrepancies in assessing the paper’s suitability, the team members decided to include the questionable articles in the full content analysis. After this operation, 1072 papers remained in the second step. Before a full-content analysis, duplicate records and review papers were removed.

In the second step of the screening process, the authors examined the papers in the full-text research. The main aim was to assess their relevance to the investigated thematic area. Papers were evaluated based on their contributions to understanding DT applications, methodologies used, and their implications for maintenance and operational practices in transportation systems. As in the first step, the research teams made the evaluation individually. Later, at research team meetings, we compared team members’ opinions. In case of discrepancies in assessing the paper’s suitability, the team members focused on a more detailed analysis of the full document. As a result, 730 papers were excluded for specific reasons. For example, the studies that describe maintenance issues, e.g., medicine applications, were excluded.

After the screening process, 201 publications were selected for further qualitative and quantitative analysis. A cross-sectional review of the identified papers was also conducted to ensure we accumulated a relatively complete census of the relevant literature [

]. As a result of the analysis carried out, it was confirmed that the identified publications provide a complete state of the art in the research area analyzed.

represents the flow diagram of the selection of studies according to PRISMA statements. The PRISMA checklist is available in

PRISMA-based flowchart of systematically selecting relevant studies in the analyzed research area. Source: own contribution based on [

This phase includes steps 7, 8, and 9 of the conducted SLR study. A bibliometric analysis was performed as part of the performance in step 7.

Bibliometrics is a branch of scientometrics that uses mathematical and statistical methods to assess the performance of scientific activities. The bibliometric analysis allows for us to study the networks formed around the most representative keywords. It presents how citations, scholars, affiliations, counties, and publications indicate the importance of specific topics in the field of research. At the same time, we can see a noticeable increase in interest in bibliometric studies in science (see, e.g., refs. [

Following the analysis, the selected articles were stored, documented, and classified using the Mendeley reference manager [

]. The primary content-based analysis was performed using MS Excel Professional Plus 2019 software and VOSviewer ver. 1.6.18 software [

]. The main results are presented concerning, among others, the authors’ location, publication time, or number of citations. The citation overview was made based on the Google Scholar database.

], VOSviewer is a program developed for constructing and viewing bibliometric maps that can be examined in full detail. The quantitative summary includes an analysis of the occurrence of trends. In addition, distribution by year and publication source was performed. Following the functionality of VOSviewer software, we constructed bibliometric maps and examined them in detail. The distance-based bibliometric maps that were created focus on keyword co-occurrence and relations between main authors. The results are presented in

Step 8—synthesis of research findings was performed. The obtained outputs were discussed in relation to the four defined research questions.

The last step is connected with the development of this study with a clear definition of its limitations and directions for further research. The results of step 8 and 9 are presented in

. They constitute the basis for developing the framework for DT-based maintenance management of transportation systems in the context of internal transportation performance.

This section includes the results of the conducted systematic review according to the defined research methodology (

In the first step, a bibliometric analysis of already-selected publications for further research on the topic of DT use in the transportation sector was carried out. A total of 201 publications from the seven subject areas analyzed were accepted for detailed analysis. The largest number of articles (44 papers) was in the area of the link between DT and land transportation (road). The number of analyzed publications in the other areas is as follows: in the area of railway transportation—38 publications; air transportation—37 publications and in-house transportation—34 publications; water and intermodal transportation—19 publications; and in the area of supply chains operation, 14 publications. To the last group, “other applications”, 15 publications were assigned.

The analysis of the authors’ and scientific centers’ origins was also a part of bibliometric analysis. The carried out analysis shows clear differences in scientific activity around the world. China definitely dominates in terms of the number of publications, as the number of papers coming from this country accounts for 25% of all items analyzed. There is also strong scientific activity in the United States and Germany, with 17 papers each. Other countries have varying levels of publications, including Australia (16 papers), England (12 papers), India (8 papers), Spain and Italy (7 papers each), South Korea and Russia (6 papers each), Poland (5 papers), and Brazil (4 papers). The regions of origin of the authors of the analyzed publications are shown in

. Analyzing the scheme in terms of continental division, the largest number of articles comes from Europe, accounting for 49% of all publications. Asia also shows high publication activity in the area, with 37% of the analyzed articles coming from there. In contrast, 10% of publications come from North America, 8% from Australia, about 3% from Africa, and less than 3% from South America.

A number of papers by the location where the investigated study took place.

The dominance of certain countries in the number of publications related to digital twins (DTs) may indicate increased research intensity as well as investment in DT technology in these regions. Countries such as China, the United States, and Germany have been investing in scientific research and technological development for many years. Digital twins are an advanced technology that requires significant financial resources, research assets, and access to advanced infrastructure, which is possible in these countries due to well-developed research and industrial ecosystems, as well as strong governmental support. Government support is reflected in numerous research and innovation funding programs aimed at implementing strategies such as “Industry 4.0”.

The predominance of publications from Europe and Asia may lead to a limited perspective, focusing primarily on issues, solutions, and research contexts characteristic of these regions. A lesser representation of research from other parts of the world, such as Africa or Latin America, may result in the omission of specific challenges and opportunities related to digital twins in various cultural, economic, and technological contexts. Additionally, research on digital twins often concentrates on sectors that are highly developed in the leading countries, such as manufacturing, automotive, or advanced technologies. Other sectors, such as education, agriculture, or public services, may be less explored, leading to gaps in the literature and potential underestimation of DT applications in these areas. Moreover, most scientific publications are in English, which may exclude important research conducted in other languages. This can lead to the oversight of significant findings and perspectives from research conducted in countries where English is not widely spoken.

This review brings together 201 publications that were published between 2017 and 2024.

illustrates the distribution of the publications according to their publication year. As we can see, a significant number of publications (173) were published between 2021 and 2024. In 2024, the analysis includes articles published until June, accounting for 59% of the articles published in 2023. Given that the data cover only the first half of the year, it can be predicted that the total number of publications this year may be higher than the previous year.

In addition, the studied articles were published in 142 journals.

shows the graph of a list of journals in which at least two articles were published in the area under study. Eighty-eight articles from 31 journals were analyzed. During the analyzed period, the largest number of publications appeared in the journal

(11 articles). The second highest number of publications in the studied area was in the journal

Engineering Applications of Artificial Intelligence

published four articles each. In comparison,

published three articles each. The remaining publishing outlets published two articles each on the topics under study.

Number of publications with journal sources (for journals with at least 2 published articles out of the 201 articles analyzed).

) promote an interdisciplinary approach to scientific publications. This makes them ideal venues for publishing research related to digital twins (DTs), which, as a technology with a broad range of applications, integrates aspects of engineering, computer science, and systems management. The primary focus of articles accepted and published by

revolves around sensors and monitoring systems, which are crucial for the development of DTs. Consequently, it is natural that the highest number of publications in the analyzed area has appeared in this journal. Additionally,

is dedicated to new technologies related to IoT, which is an integral component of digital twins. A DT utilizes IoT for real-time data collection, making this journal a fitting platform for research in this field.

are journals with strong connections to industrial applications and applied engineering. DTs are significant for industries, especially in areas such as automotive, manufacturing, and engineering systems, which explains their presence in these journals.

The high number of publications in these journals may also indicate their prestige and broad visibility within the scientific community. Authors may prefer to publish their work in widely read and respected journals, which enhances the impact of their research on the development of digital twin technologies.

To supplement the conducted analysis, a co-occurrence of authors was investigated using VOSviewer software and Excel software. For the selected papers, 81 authors were identified. In

, results are presented for 15 authors who had the largest set of co-authorship links. The largest set of links (18) has four authors: Bernal Esteban (co-author of three papers [

]), Cole Colin and Maksym Spiryagin (co-authors of four papers [

]), and Qing Wu (co-author of four papers) [

]. All authors are from Australia. In addition, the distribution of publications per number of authors per paper is given in

. This research indicates that multi-author articles predominate, especially those written by teams of three to five authors. Single-author articles are in the minority, suggesting that research papers are more often carried out in teams than individually. As can be seen, very large research teams (more than five authors) occur less frequently in the analyzed sample of publications.

The largest set of connected items based on co-authorship links. Source: own development using VOSviewer software [

Distribution of publications per number of authors.

The last part of the bibliometric analysis was a keyword co-occurrence analysis based on using VOSviewer software. The initial study focused on the keywords that occurred in the publications at least once. As a result, 609 keywords were identified for the selected papers (

Mapping of the keywords that have occurred in the selected publications at least once. Source: own development using VOSviewer software [

The results present the used keywords in 67 clusters. The most used words were digital twin (121 links), digital twins (20 links), and Industry 4.0 (15 links). Also, the words “machine learning” and “predictive maintenance” occurred frequently (12 links with total link strength equal to 76). One of the largest clusters of publications (27 items, red one in

) underscores the significance of digital twin technology integrated with machine learning and deep reinforcement learning. It emphasizes the transformative potential of digital twins in various fields, from building management and logistics to transportation and aerospace, highlighting their role in efficiently monitoring, modeling, and optimizing complex systems. The second largest cluster of publications (27 items, green one in

) revolves around applying digital twin technology to mobile robots, automated guided vehicles (AGVs), agile manufacturing, supply chain management, and vehicles. Central to these studies are various modeling methods, including virtual models, advanced simulation, fuzzy logic, genetic algorithms, graph theory, and trajectory optimization, which are employed to enhance the effectiveness and precision of these systems. The third interesting cluster of publications (26 items, blue one in

) focuses on applying digital twin technology in maintenance, repair, risk analysis, and decision-making. Central to these studies are various methodologies, including time series analysis, stochastic optimization, inspection processes, and integration with cyber–physical systems, electric vehicles, battery capacity, and battery management.

A more detailed analysis was focused on the keywords with the largest occurrence sets (

). The results present the 30 most frequently used keywords in seven clusters.

Mapping of the keywords with the largest occurrence. Source: own development using VOSviewer software [

The largest cluster (seven items, red one in

) is strictly connected with applying digital twin technology in the aviation industry and the problems of condition monitoring, diagnostics, and predictive maintenance. Central to these studies are data-driven approaches and advanced techniques such as machine learning and deep learning, which enhance the accuracy and efficiency of monitoring and diagnostic processes.

The second cluster of publications (six items, green one in

) centers on the application of digital twin (DT) technology within the context of Industry 4.0, focusing on analytics, the Internet of Things (IoT), prognostics, simulation, and supply chain management. This cluster highlights the transformative impact of digital twins in modern industrial landscapes, where interconnected systems and data-driven decision-making are paramount.

The third cluster (six items, blue one in

) focuses on the innovative convergence of digital twin technology with blockchain, maintenance strategies, reinforcement learning, and railway systems. This multidisciplinary approach highlights the potential for enhancing railway operations’ efficiency, security, and reliability through advanced digital solutions. It highlights how these technologies can work together to provide secure, transparent, and optimized solutions for managing complex systems (including railway systems). Integrating digital twins with blockchain ensures data integrity and trust, while reinforcement learning enhances adaptive maintenance and operational efficiency, ultimately leading to more reliable and efficient services.

At the end, the fourth cluster (four items, yellow one in

) explores integrating digital twin technology with battery management systems in the context of electric vehicles (EVs). This interdisciplinary research highlights how digital twins can significantly enhance the performance, efficiency, and reliability of battery systems in electric vehicles.

The performed bibliometric analysis introduces the comprehensive content-based analysis, which is carried out in the next section.

As a result of the conducted research, seven core research areas were defined, which have been most extensively developed over the last seven years (

The main areas in the context of the transportation digital twin in maintenance. Source: own contribution.

Due to the rapid development of the aviation industry, the expansion of aircraft fleets, and the design of increasingly complex operational processes in the air transport sector, a need to utilize advanced technologies that support the maintenance management of aviation systems has arisen. With the growing availability of data from various aviation processes, a technology that has begun to be employed in recent years to achieve these goals is the digital twin. Given the need for continuous monitoring and improvement of complex aviation systems, DTs are frequently used by aircraft manufacturers, airlines, and airport operators. In the aviation sector, the application of DT technology is broad. An overview of the possibilities of using DTs for the aviation zone can be found in [

], the development and goals of DTs for airports are presented. In [

], the challenges associated with digitization and the implementation of DTs in the aviation industry are discussed.

shows the main areas of DT application in the aviation sector.

The main areas of DT implementation in the aviation industry. Source: own contribution.

DT has found its application in the aviation sector in producing flying objects, providing numerous benefits for manufacturers, such as increased efficiency, optimization of production processes, and design process improvement. The general structure for intelligent planning of processes related to the production of aviation parts based on the DT concept is described in [

]. The use of DTs for the ground control system of an aircraft’s nose landing gear to assess the accuracy and integrity of the steering angle estimation for various control algorithms is presented in [

]. It has been demonstrated that for these purposes, the soft computing algorithm exhibits higher accuracy compared to least squares algorithms. In [

], the specification of DT for a shared workspace for humans and robots, where electromechanical actuators are mounted on an aircraft wing, is presented. A DT of an aircraft’s power electronics cooling system (PECS) for the optimal placement of sensors in this system was introduced in [

DTs play a significant role in monitoring the technical condition of aircraft and in real-time maintenance forecasting and optimization. This capability allows for quick responses to emerging anomalies and minimizes the risk of aircraft failures, thereby reducing airport downtimes. In [

], a method for analyzing data from measurement devices installed on board an aircraft using a DT is presented. The DT of an aircraft engine for fault detection, isolation, and identification is described in [

], a diagnostic algorithm for the electrical power system in an aircraft was developed to detect faults and their root causes, where one of the creation stages involves developing a DT of the electrical power system. Ref. [

] discusses the use of DT for diagnosing and forecasting the technical condition of aircraft electrical equipment. In [

], the authors focus on the use of DT in monitoring the power system of civil aircraft. Meanwhile, ref. [

] describes the application of smart devices in aviation maintenance utilizing virtual reality (VR) and a DT. The authors of [

] designed a graphical user interface for a system using an aircraft DT and augmented reality glasses for its maintenance and repair. In [

], the DEVOTION methodology for DT development was proposed. The authors developed an extensible DT platform to ensure the electrical and electronic systems for space launch vehicles are secure. The authors of [

] developed a DT-based system to investigate the problem of dynamic resource allocation for the communication needs of vehicles assisted by unmanned aerial vehicles (UAVs) and reconfigurable intelligent surfaces (RISs). This approach reduced energy consumption and minimized transmission errors in variable environments. In [

], discussions on how DTs can improve monitoring, damage assessment, and decision-making in aircraft design, maintenance, and fleet management are provided. The authors of [

] proposed a modular DT architecture for aircraft supporting maintenance processes. In [

], an analysis of fatigue life prediction for an electric motor shaft in an airplane was conducted using a DT of the rotor shaft in the electric motor to simulate the stresses encountered. A DT of the fan blade grinding process in an aircraft is presented in [

], where the DT was developed to study the required grinding parameters. In [

], an aircraft DT was introduced to determine safety and reliability. The article also describes the current state of knowledge on DT risk assessment modeling for critical fatigue areas. The DT of an aircraft’s nose wheel for optimizing maintenance processes was developed in [

] describes a simplified method for diagnosing faults in any aircraft system using a DT based on the Open System Architecture for Condition-Based Maintenance. This concept was tested on three different systems. In [

], a DT supported by a multiscale residual self-attention feature fusion network for diagnosing damage in hypersonic flight vehicles is presented. A method for characterizing damage using sensors from various locations was developed in [

] to predict the damage’s location, size, and orientation. This method supports the creation of aircraft DTs for diagnosing damaged structures. Determining the remaining useful life of aircraft maintenance parts using various data analysis methods combined with a DT is presented in [

], a system for tracking aircraft spare parts throughout the supply chain and the structure of DT integration into the proposed system is proposed.

] presents the development of a general model for managing the mobility of electric air vehicles. A DT is used here to simulate and optimize air mobility. Ref. [

] discusses the application of DTs for training deep reinforcement learning (DRL) models to enable the collective movement of multi-drone UAV systems, where DTs facilitate the rapid deployment of trained models to real UAVs.

In recent years, significant progress has been made in the railway transport sector regarding digital transformation, particularly in implementing digital technologies and data utilization. For railway transport, DTs have great potential in supporting the management of railway infrastructure, operational processes, and passenger safety.

illustrates the identified main areas of DT application in the studied transport sector.

The main areas of DT implementation in the railway industry. Source: own contribution.

The railway sector is one of the areas where DT technology is most frequently used in the maintenance management of railway assets. This is confirmed by numerous publications summarizing recent developments in this area. For example, Ref. [

] describes an overview of the possibilities of DT technology and its implementation in transforming railway maintenance and digitizing railway infrastructure and signaling. In [

], the activities of the Railway Technical Research Institute regarding the maintenance technology of the power system in electric railways are described. They propose DT technology to predict and assess the progress of degradation. A review of published research on the application of artificial intelligence (AI) in railway transport is presented in [

]. The authors highlight DT and the Internet of Things as the main technologies supporting AI. For other reviews, the authors recommend reading [

Most works in the area of DT application in the railway sector aim to monitor the condition of machinery and predict anomalies. The architecture for managing the condition of rail vehicles based on DT is presented in [

], the use of DT is aimed at optimizing maintenance processes. Ref. [

] focuses on developing methods for diagnosing faults in rail vehicles using supervised machine learning. In [

], the use of a DT for simulating substitute wagons was proposed to reduce the computation time required to assess the safety of the entire train. The DT was used to eliminate data gaps, which enabled the creation of a dataset necessary for training the model. A DT for railway systems was proposed in [

], a DT of the heating, ventilation, and air conditioning system is described to monitor the condition of this system. In [

], a DT of a high-speed train bogie was presented to determine the operational conditions of such a bogie based on the analysis of vibration signals. The work also describes techniques for processing vibration signals. Ref. [

] presents the concept of a DT locomotive in the context of operation and maintenance management systems. In [

], a DT was applied in managing wireless networks of smart railways, where the DT enables these networks’ design, optimization, and lifecycle management. In [

], a DT was used to accurately predict the mass of solid particles in air filters in a passenger car, monitor filter wear, and identify faults.

Rail tracks play a crucial role in railway transport as a fundamental element of railway infrastructure. They perform essential functions necessary for the safe and efficient movement of trains. Therefore, in [

], a predictive model for the life of railway wheels and rail tracks is presented, which could be a part of a future digital twin of the railway system. In [

], a DT was used to correlate the assessment of visual conditions with mechanical performance. Meanwhile, in [

], a simulation modeling method was proposed for predicting rail surface damage based on the DT of a locomotive. In [

], a DT for simulating the dynamics of railway vehicles, particularly in the context of calculating surface damage to rails, was discussed. The assessment of the condition of railway tracks and their maintenance-free 3D reconstruction using a robotic system was presented in [

]. This research can be used as an autonomous generator of twin models, leading to improved railway maintenance DTs and intelligent railway infrastructure management. In [

], various approaches to modeling vehicle–track interactions and predicting rail damage were discussed, with DTs responsible for integrating and optimizing simulation models. Ref. [

] addresses the use of DT for simulating complex guided wave propagation in railway tracks under different conditions.

A railway switch is crucial in the railway transport system, enabling trains to change tracks. Switches must be well-maintained and functional to ensure the safe and reliable operation of the railway system. Regular maintenance and proper monitoring and control of switches are necessary to ensure the smooth flow of railway traffic and minimize the risk of failures. Consequently, several studies have focused on monitoring the condition of this specific element of railway infrastructure using DTs. In [

], DT-assisted fault diagnosis structures for railway point machines (or railway switch machines) are presented. Ref. [

] introduces a solution for monitoring temperature conditions and other atmospheric factors to make the DT of railway switches more accurately reflect reality. In [

], the use of a DT is described as part of a six-dimensional BIM model for a railway switch system.

] presents the application of reinforcement learning with a DT for optimizing the efficiency of railway infrastructure maintenance. In [

], the structure of a DT for urban railway transport and its implementation method are described. The concept of a DT for railway infrastructure is presented in [

]. To improve documentation accuracy and reduce human errors in the operation and management of railway infrastructure, ref. [

] discusses using a DT of a test railway track. Ref. [

] outlines a framework for designing and implementing DTs in railways. A smart railway station DT concept is described in [

] focuses on building an integrated model for data, models, and knowledge management to enhance railway project analysis and intelligent management. This enables dynamic linking and global searching for connections across extensive spaces. In [

], the application of the DT concept in railway control systems is discussed, with the authors primarily focusing on modeling and simulating railway signaling system elements. Refs. [

] demonstrate the use of DT for real-time monitoring of the structural integrity of railway bridges, allowing for early damage detection and optimization of maintenance actions. Meanwhile, ref. [

] describes the implementation of DTs for railway bridges in Germany, which is aimed at forecasting their condition and structural safety and optimizing maintenance efforts. Ref. [

] presents the potential to improve passenger safety and pedestrian traffic management at train stations through DT as a decision-supporting tool.

In a DT, the integral acquisition of data is crucial, as it forms the foundation for assessing the condition of the object under investigation. Therefore, the authors in [

] presented a new approach based on Internet of Things technology for intelligent data acquisition to generate DTs in the railway industry.

In the case of land transport, digital twins can serve as a tool with significant potential, enabling effective and intelligent management of infrastructure and vehicles.

illustrates the main areas of DT application in land transportation.

The main areas of DT implementation in land transportation. Source: own contribution.

Many of the publications selected for this literature review focus on electric vehicles and battery management. The authors in [

] reviewed various DT applications in the electric vehicle industry. A review of publications describing the use of DTs for battery management was conducted in [

], DTs for electric vehicle batteries are presented for energy consumption research, battery capacity estimation, and technical condition prediction. Meanwhile, DTs of electric vehicles for simulating realistic events that may occur in the real world is discussed in [

]. The authors concentrated on simulating electric vehicles’ charging and discharging processes during use. As a result of these simulations, it becomes possible to plan the charging of electric vehicles and to plan the placement of charging stations. DTs of electric vehicle batteries are described in [

], the authors also proposed using a DT during the battery production stage. The DT of the production process facilitates the development of production lines and workshops to streamline the entire manufacturing process. Furthermore, a DT for electric vehicle battery management systems was proposed in [

], a DT for an electric vehicle engine was developed to monitor and predict its condition. The authors in [

] addressed a broader area, focusing on DT for electric drives. Additionally, there is a study discussing the challenges of implementing electric vehicles. The authors in [

] highlight that a significant obstacle to the mass adoption of such vehicles is their complex internal structure, which makes the repair and maintenance of electric vehicles difficult and costly. To address this, the authors propose using a DT in servicing and repairing electric vehicles, significantly reducing time and associated costs.

DTs also support the development of connected and autonomous vehicles. Through simulations and machine learning, virtual testing and training for autonomous systems can be conducted, accelerating their development and introduction on the roads. DTs enable vehicle behavior analysis in various scenarios, allowing for the refinement of control algorithms and increasing road safety. In [

], comprehensive research on the application of DTs in autonomous vehicles is presented. The role of DTs as a development environment in improving the performance of autonomous systems supported by artificial intelligence is explored in [

] describe already-published applications of DTs in automated vehicles and intelligent transportation systems and the opportunities and challenges associated with applying DTs in automated vehicles. Ref. [

] discusses the methodology for creating and integrating smaller DTs for autonomous vehicle functions and examines the challenges related to their integration. In [

], a DT framework based on edge infrastructure for autonomous vehicles is presented. The topic of optimizing electric drivetrains in autonomous vehicles is addressed in [

], where the authors mention the potential use of DTs and virtual reality to monitor the condition of drivetrains. A comprehensive framework for the navigation of autonomous vehicles in infrastructure construction scenarios using DTs is outlined in [

] investigate the sources of unpredictability in the motion trajectory of DTs for connected vehicles.

] present the potential of DTs in vehicle condition management. They confirm that DTs can be utilized to assess the status of complex systems. The integration of DTs with predictive maintenance methods is discussed in [

]. A DT for fault detection is proposed in [

], where the authors suggest combining a DT and failure mode and effect analysis (FMEA) for online diagnostics of vehicles. In [

], a DT for diesel engines is developed to detect and predict anomalies in the driveline operation. The role of DTs in predictive maintenance is outlined in [

], focusing on the maintenance of automotive brake pads. The use of a DT for electric machines for educating electrical engineers is proposed in [

]. By analyzing data generated by the DT, students learn to diagnose potential failures or malfunctions of the machine. The development and validation of a DT for steel railway wheels, allowing for fatigue life prediction, is presented in [

] describes a DT for predicting real-time vehicle fuel consumption.

] introduces a holistic approach to managing logistics processes within an industrial park using a DT of the production logistics system. This study emphasizes the transportation phase within the industrial park. The proposed solution aims to synchronize information from various units in the industrial park to enable effective transportation decision-making between them. In [

], the authors suggested using digital twin in intelligent transportation systems to improve road traffic. In [

], the focus is on DTs in intelligent transport systems. Applying this technology allows for all real-world elements to be replicated in the virtual environment, including road infrastructure elements, human-driven vehicles, and autonomous vehicles. The authors of [

] have a similar goal, where the DT includes people, vehicles, and road traffic. The result of this work is a proposal for a mobility digital twin structure. In [

], a DT for managing data about road infrastructure elements is proposed. Meanwhile, ref. [

] utilized DT for rapid iteration and validation of collision avoidance systems in intelligent vehicles, enabling improved safety and reliability of such systems. Additionally, ref. [

] describes an approach to managing business processes by developing an organizational DT. This approach integrates business processes with models, ensuring reliable road freight transport in an unstable external environment. An intriguing topic is addressed in [

], which focuses on modeling driver behavior on highways using DTs as it is stated e.g., in [

], a DT detects potential anomalies and predicts and simulates accident scenario. This topic is reviewed in [

]. A DT for forecasting passenger flows in public transport systems is presented in [

], allowing for more precise transport infrastructure planning. The authors of [

] took a comprehensive approach by proposing a telemetry platform based on a DT in the transport sector. This platform monitors fuel consumption, pollutant emissions, and driver practices.

Supply chain cooperation is a crucial element for the success of many industries, both at the local and global levels. Modern challenges, such as the rapid pace of change, increasing customer demands, and the complexity of logistics operations, present new hurdles for companies. The advancement of technology and the emergence of modern solutions positively influence the visibility of the supply chain and help address these challenges. One technology that supports improving supply chain operations is the digital twin (DT). Three review papers have been published in this research area. In [

], the authors present the benefits enterprises can gain by implementing DTs in their logistics supply networks. The findings from the article demonstrated that implementing DTs would enhance visibility within their logistics supply networks. All four factors of organizational visibility (visibility for sensing, learning, coordination, and integration) would improve by developing predictive indicators, forecasts, diagnostics, and descriptions of physical resources for the enterprise’s logistics. The paper also discusses the challenges associated with DT implementation and proposes solutions to overcome them.

] addresses the evolution of research trends in applying DTs in supply chain management. The authors identified ten themes within these research trends. After conducting a literature analysis, it was concluded that DTs are a key factor enabling the development of resilient supply chains. Meanwhile, ref. [

] describes the impact of DTs on the supply chain and the prospects for DTs in logistics. It also presents the main barriers and opportunities for applying DTs within the supply chain. Additionally, the authors propose a framework for utilizing real-time data to generate the data streams necessary for creating a real-time operational DT.

The remaining papers selected for review in this area mainly focus on the architecture of DTs in supply chain logistics [

] proposes a digital twin supply chain framework encompassing multimodal supply chains. In [

], a disruption identification model based on a DT for the supply chain is proposed. The authors of [

] developed a DT structure for risk management in logistics systems. This structure aims to create a virtual resource based on building information modeling (BIM) to monitor the ongoing progress of modular construction. The authors of [

] examined the conditions related to the design and implementation of DTs in the context of managing disruption risks in the supply chain. In [

], a DT-based intelligent cold chain management platform is described, showcasing its application in a pharmaceutical distribution center, where storage conditions, personnel safety, and product quality are monitored. Lastly, ref. [

] investigated the technical implementation of an autonomous supply chain system based on multi-agent systems (MASs) and DTs. And, at the end, Ref. [

] presents an evolutionary game model utilizing DTs for participants in a crowdsourcing logistics scenario. This learning method allows for the optimization of crowdsourced logistics.

4.2.5. DTs in Water and Intermodal Transportation

In maritime transport, a key sector of the global economy, modern technologies are also being implemented. Digital twins are increasingly utilized in this sector, as they enable better management and optimization of operations, as well as improved safety and increased efficiency. A significant portion of the publications selected for this literature review focuses on monitoring the condition of technical objects.

], the issue of monitoring the performance of marine engines is addressed. The authors propose a method for monitoring engine status based on a DT. After analyzing the results obtained from the engine’s DT, they confirm the validity of using this method, as the difference in accuracy between DT and real data is negligible compared to the costs incurred when monitoring engine status using other methods. Authors in [

] designed a marine engine sensor diagnostics and condition management concept. The solution proposed in the article allows for intelligent engine monitoring, advanced sensor fault detection, and precise maintenance planning. In [

], a framework for assessing the technical condition of marine engines using a DT was developed. The approach presented in [

] involves using a DT to monitor and predict fatigue damage specific to the vessel. Based on computational models that incorporate ship position data as well as meteorological and oceanographic information, it is possible to track the accumulation of fatigue in the vessel over time, make operational decisions, and plan maintenance. Additionally, in [

], the application of DT for diagnosing faults in autonomous water vehicles under real-world conditions is described. The case of unmanned surface vehicle DT development is given in [

In maritime transport, digital twins can also be applied at the level of port infrastructure. This enables better planning and optimization of loading and unloading processes for ships, managing traffic within the port, and forecasting resource requirements. Publications have also emerged that describe the use of DTs in intelligent ports. In [

], the authors analyze and propose directions for applying DTs in ports, focusing on their utilization in the construction and operation of ports. They also highlighted issues related to decision-making in construction within this sector. A model for managing intelligent ports based on DTs is presented in [

], where the authors explored the potential applications of DTs in managing port processes. The analysis indicates that DTs can be used to manage cargo transport operations and container terminal activities. It also facilitates risk prediction, communication, data sharing based on DTs, and managing processes to enhance environmental protection and sustainable development efforts.

A decision support system for assessing port resilience and optimizing repair activities based on a DT was introduced in [

] discusses optimizing lock maintenance in river systems using a DT.

] presented a structure for optimizing operations and safety in transshipment terminals where a DT is employed. The application of DTs in transshipment terminal operations enhances the efficiency of processes. In another study, ref. [

] proposed the integrated maintenance decision-making model for cranes most commonly used in container terminals. A DT is utilized in this model for maintenance purposes, aiding in aligning the maintenance schedules for the analyzed equipment. In addition, ref. [

] developed a framework for monitoring the operational status of port cranes based on a DT. Lastly, ref. [

] proposed an automated structure for planning storage areas using digital twins for uncertain port shipments. This structure optimizes warehouse space, automated stacking cranes (ASCs), and automated guided vehicles (AGVs).

], the authors propose and test, in a real application of an unmanned underwater vehicle (UUV), a general process for determining a subset of components needed for maintenance (triage) based on a digital twin (DT). This process leads to an increase in the reliability of the entire system. The authors frame the design problem as a multi-objective optimization problem utilizing experimentally determined data and metrics from a real UUV system model.

Internal logistics activities are crucial to any organization, enhancing productivity and operational efficiency. At the same time, internal logistics encompasses various activities directly related to implementing material flows within the enterprise. This requires the use of various material handling and storage equipment. The classification of the main application areas of digital twins (DTs) in in-house logistics is presented in

. A review of DTs in internal transport systems is presented in Ref. [

]. Meanwhile, DTs in logistics is discussed in [

The main areas of DT implementation in in-house logistics. Source: own contribution.

] investigate the components of a logistics hub digital twin (DT) and analyze various implementation possibilities of DTs in logistics infrastructure. In [

], network requirements for real-time data streaming and processing to generate DTs were examined. The architecture of a control system for inspection robots and methods of its implementation were also presented.

A significant portion of the topics researchers discuss regarding the use of DTs in this area focuses on mobile robots. As mentioned in [

], DTs in the maintenance of mobile robots can be used for several purposes, including predicting the battery level of a mobile robot, 3D visualization of robot calibration, and collision detection in robots. The authors of the article presented a DT that predicts when a failure will occur. In [

], a universal DT architecture for automated guided vehicles (AGVs) was introduced to design, manage, and forecast performance. A system for monitoring multiple mobile robots based on a DT to detect collision-prone movements in robots was presented in [

], a DT was used to propose a method for optimizing the motion trajectory of mobile robots. Control of AGVs in production systems was discussed in [

]. Additionally, an architectural structure was proposed to facilitate the automatic generation of a DT. In [

], the application of a DT for monitoring and predicting navigation errors in mobile robots was described. The DT structure presented in [

] is responsible for the remote programming and operation of AGVs. The DT model for simulating events in a system using AGVs, as explained in [

], is intended to test new vehicle management policies. In [

], the authors proposed comprehensive support for the AGV system using the DT model of that system. In the DT of the AGV system, it is possible to manage transport orders, select vehicles, and control the driving process. The focus of [

] was on evaluating the correctness of design assumptions in the early phases of deploying autonomous mobile robots (AMRs). A description of creating a DT for a control system for robots designed for inspecting complex working environments can be found in [

] presented a DT design for a system consisting of an assembly part and AGVs. This system allows for the selection of one of the AGVs and predicts AGV failures. A DT was also developed for robotic linear actuators to detect undesirable events [

], a mathematical model for managing cranes’ logistics and maintenance processes was developed. In [

], a DT framework for monitoring indoor air quality was proposed. The use of a DT for scheduling and collision-free routing of AGVs in a variable environment is described in [

]. A model for simulating external metamorphic constraints in underground transport using mobile robots was presented in [

The proposal of a decision support tool based on a DT for internal logistics operations and maintenance logistics is presented in [

] analyzed aspects of DT application in warehouse management. In [

], the DT’s decision-making support focused on processes related to the design and analysis of logistics operations. A smart material distribution management system based on DTs was presented in [

], while logistics distribution was discussed in [

], the authors discuss the use of a DT for dynamic planning in large machining workshops. In [

], a DT-based monitoring and alert system for refrigerated logistics warehouses was introduced. The role of the DT, in this case, is to optimize the freshness and energy efficiency of stored products. Authors in [

] proposed a DT framework for human-building integration activities to optimize building maintenance. In [

], the design and implementation process of an evaluation algorithm for a continuous transport system DT was presented, enabling monitoring and correcting belt conveyor voltage asymmetry.

] introduced a remote monitoring system for augmented reality. The purpose of this system is to assist inexperienced operators in understanding data from the DT. In the context of DT application in maintenance, researchers also presented the possibility of using a DT to train new maintenance workers for highly automated systems [

], a platform supporting a DT for monitoring safety on premises was developed.

The last group of publications selected for analysis includes 15 articles that were not classified into previous groups. Some of these publications address components or parts used in various transportation sectors. On the other hand, there are also individual works related to specific industrial sectors.

The induction motor has a wide range of applications. It is used in railway, road, and internal transportation. In [

], a digital twin (DT) of the induction motor was proposed for creating databases of its failures, as diagnosing the causes of induction motor failures and monitoring its characteristics during operation is very complex. This requires collecting data from the same motor both when a failure occurs and when it does not. Meanwhile, a tool designed for the maintenance of electric motors based on a DT is presented in Ref. [

], a DT is used for detecting inter-turn short circuits in the stator of an alternating current induction motor. Ref. [

] describes a DT for monitoring and predicting the degradation state of fuel cells. In addition, a DT structure for the reliability of lithium-ion batteries is proposed in [

One of the components of rotating machines, such as rotors (e.g., wheels), turbines, and internal combustion engines, is the bearing. The structure for diagnosing faults in such bearings when error data are unavailable is presented in [

], the combination of a DT and a machine learning algorithm was developed to diagnose bearing cracks’ type and size. Similarly, in [

], the authors focused on a DT of bearings.

Several publications also address the use of DTs in maintenance within the mining industry. A DT framework for real-time monitoring of mining trucks is presented in [

], a methodology for assessing the wear of gear tooth surfaces based on DTs is described. Ref. [

] presents the DT of the braking system in mining hoisting equipment. In [

], the possibility of using DTs to diagnose rolling bearing faults is discussed.

] describes the use of DTs in developing autonomous agricultural vehicles.

In addition, two papers focus on general complex devices. In [

], the use of a DT for assessing the technical condition of industrial machines is described. Meanwhile, the intelligent maintenance of complex devices using blockchain technology and DTs is presented in [

The main aim of this paper is to conduct a comprehensive review of the existing literature to provide a substantive analysis within the key areas of digital twin (DT) applications in the maintenance of transport systems. A total of 201 articles meeting the established selection criteria were reviewed, allowing for an in-depth examination of the analyzed issue. Such deep analysis gives the possibility to answer the stated research questions:

RQ1 intended to discover the leading trends in DT concept implementation in transportation systems O&P and investigate its evolution over the last decade. The main research outputs here are discussed broadly in

In the defined seven application areas, the scope of issues covered is very complex, ranging from the presentation of technological solutions dedicated to predictive maintenance, condition monitoring, and forecasting to issues related to the analysis of acquired data and the need to make complex operational decisions (e.g., connected with path planning). In the studied years, the smallest number of publications regarding the use of DT technology was noted in supply chains and water and intermodal transport. These areas appear to be particularly promising for the further development of DTs. In contrast, the remaining research areas (i.e., air, rail, land, and internal transport) show a similar number of publications. Additionally, interest in these areas has been increasing over the years.

Focusing on the comparison of DT implementation across the domains of aviation, rail transport, road transport, supply chain operations, water transport, and in-house logistics reveals both similarities and differences in how this technology is leveraged to enhance operations, safety, and efficiency. The main similarities are visible in the following three main subareas: condition monitoring and predictive maintenance, process optimization, and integration with IoT and real-time data analytics.

Across all the analyzed sectors, DTs help monitor the condition of machinery, infrastructure, and systems, enabling proactive maintenance that minimizes downtime and improves reliability. For instance, in maritime transport, a DT is used to monitor marine engines and predict fatigue damage to vessels, while in rail transport, it ensures the safety and stability of rail infrastructure. In in-house logistics, DTs monitor the status of mobile robots and equipment, ensuring smooth internal operations.

Process optimization is another key area where DTs are widely applied. Across all sectors, DT technology is leveraged to streamline operations, whether in optimizing production processes in aviation, enhancing energy management in road transport, or improving port traffic management in maritime transport. Similarly, in supply chain operations and in-house logistics, DTs are used to optimize logistics and warehouse management, leading to more efficient and effective operations.

Additionally, DTs in all these sectors are integrated with IoT systems and real-time data analytics. This integration allows for the continuous collection and analysis of data, providing valuable insights that enhance decision-making. Whether monitoring environmental conditions in logistics, predicting equipment failures in various transport modes, or managing real-time operations in supply chains, the combination of DTs with IoT and data analytics is a common and powerful tool for improving efficiency and reliability across different industries.

A summary of the main differences identified in the analyzed transportation sectors in the context of DT implementation.

DT applications in aviation are broad and complex, encompassing design, production, fleet management, and training. The use of advanced technologies like VR/AR and complex data analytics is prominent in this sector.

DT applications range from predicting component life to modeling risks in critical areas such as fatigue.

Integrates advanced technologies like VR, AR, and complex algorithms to handle extensive data and simulations.

The focus is more on infrastructure monitoring (e.g., tracks, switches) and vehicle safety, emphasizing maintaining the rail network’s stability and reliability.

DT technology is heavily used for infrastructure and vehicle monitoring, focusing on safety and maintenance optimization.

Emphasizes reliable and stable infrastructure, integrating a DT with predictive maintenance and safety systems.

DTs in road transport, particularly with electric and autonomous vehicles, focus on simulating vehicle operations, optimizing energy use, and enhancing safety through predictive analytics.

DT applications are significant in electric vehicles and autonomous systems, particularly in battery management and route optimization.

Involves integrating DTs with AI and machine learning for vehicle autonomy and energy management.

DTs are critical for managing logistics, risk, and ensuring visibility across the entire network, often integrating with multi-agent systems and predictive technologies.

DT technology aids in logistics management, risk assessment, and the integration of real-time data to improve the resilience and efficiency of supply chains.

Focuses on integrating DTs with logistics systems for real-time visibility and risk management, often dealing with the complexity of multi-agent environments.

DTs are used at both the vessel level (e.g., engine monitoring, fatigue prediction) and the port infrastructure level, optimizing port operations and traffic management.

DT applications are seen in both vessel management and port infrastructure, focusing on operational efficiency, safety, and sustainability.

Incorporates DTs at both macro (port management) and micro (vessel maintenance) levels, dealing with maritime-specific challenges like environmental impact and operational safety.

This sector uses DTs to optimize internal processes, particularly in managing mobile robots (AGVs), warehouse operations, and indoor environmental conditions.

The focus is on optimizing internal transport systems, robot management, and environmental control, with DTs providing crucial support for operational efficiency and maintenance.

The integration of DTs with robotics and automated systems is crucial, with a focus on enhancing productivity and safety within controlled environments.

Based on the presented summary, providing a more detailed analysis is possible. Several papers are primarily concerned with the key terms of sensors, deep machine learning, the Internet of Things, or big data analytics. In the context of implementing digital twin (DT) technology to support the management of the technical maintenance processes of transportation means, several key areas where the digital twin approach is widely applied in transportation sectors can be identified:

Technical condition monitoring: The digital twin enables continuous monitoring of the technical condition of vehicles and transportation infrastructure. Thanks to advanced sensors and IoT technologies, the DT can collect data on part wear, engine operating parameters, and even road conditions. This allows for the quick identification of potential technical problems and failures (see, e.g., refs. [

]). This research problem is especially important for aircraft maintenance and risk management due to safety issues.

Failure prediction: Based on the collected data, a DT can perform predictive analyses, forecasting future failures and technical issues. This allows for planning maintenance activities in advance, avoiding downtime and costly repairs (e.g., refs. [

]). In addition, the main leading trends here are connected with integration with advanced technologies (like BIM and IoT in railway transportation) or structural integrity maintenance. This integration enables more accurate and comprehensive monitoring of structural health by combining real-time data from DTs with the detailed digital representations offered by, e.g., BIM. The fusion of these technologies allows for early detection of structural issues, more informed decision-making, and optimized maintenance practices, ultimately enhancing the safety and longevity of infrastructure.

Optimization of maintenance plans and schedules: Utilizing data from the digital twin, more effective maintenance plans can be developed (maintenance scheduling). A DT allows for the individual adjustment of inspection and repair schedules to the actual technical condition of vehicles, which helps reduce the maintenance costs of the transport fleet (see, e.g., refs. [

]). The main leading trends are connected with the integration of predictive analytics and machine learning algorithms as well as the use of IoT for continuously monitoring asset performance and allowing for dynamic adjustment of maintenance schedules.

Simulation and testing of new solutions: A digital twin enables the simulation of various operational scenarios and the testing of new technological solutions before their implementation in real conditions. This allows for assessing potential benefits and risks associated with introducing technological innovations in the operational activities of the transport fleet (see, e.g., refs. [

]). One of the key challenges in the simulation and testing of new solutions is the effective integration of digital twin (DT) technology throughout the entire product lifecycle. Utilizing DTs in this context requires a seamless transition from design and development to production, operation, and eventual decommissioning. Each stage presents unique demands for data accuracy, real-time processing, and system adaptability, making it difficult to maintain a consistent and reliable digital representation of the physical product. As a result, the leading trends are connected with lifecycle integration, cross-domain collaboration, validation and verification processes, or cybersecurity. This aspect is especially important for aircraft designing and production processes.

Optimization of fuel consumption and operational efficiency: A DT can be used to analyze and optimize fuel consumption and improve the operational efficiency of vehicles. By monitoring engine operating parameters, driver behavior, and road conditions, the DT helps identify areas needing improvement and implement effective fuel-saving strategies (e.g., refs. [

]). Here, one of the main trends in the implementation of the digital twin (DT) concept, particularly in optimizing fuel consumption and operational efficiency, is the increasing focus on autonomous vehicles. The integration of DT technology with autonomous systems enables real-time monitoring, simulation, and optimization of vehicle performance, leading to significant improvements in fuel efficiency. By simulating various driving scenarios and conditions, DTs help fine-tune autonomous algorithms to optimize routes, reduce idle times, and enhance overall operational efficiency. This trend is pivotal as the transportation industry moves towards greater automation and sustainability.

Remote technical support: Using remote connections and digital interfaces, the DT allows for providing technical support by experts from anywhere in the world. This enables quick problem diagnosis and provides real-time repair instructions and guidance (see, e.g., ref. [

]). Here, one of the key challenges in implementing remote support based on digital twin (DT) technology is ensuring secure and reliable two-way communication between the physical asset and its virtual counterpart. This bidirectional communication is essential for real-time monitoring, control, and feedback mechanisms that enable effective remote support and decision-making. However, establishing and maintaining such communication channels poses significant security concerns, including the risk of data breaches, unauthorized access, and cyberattacks. To address these issues, robust encryption protocols, authentication measures, and network security strategies must be employed to protect sensitive data and ensure the integrity and confidentiality of information exchanged between the DT and the physical system. Additionally, ensuring low-latency and high-reliability connections is crucial to facilitate seamless interactions and prevent disruptions in remote support services.

Operational data analysis of the monitored fleet: A DT allows for the analysis of data collected from the entire fleet of vehicles, which helps identify trends and patterns related to failure rates, fuel consumption, and driver behavior. This information can be used to implement improvements and optimize fleet management processes (see, e.g., ref. [

]). Leading trends in this area include the integration of big data analytics and artificial intelligence (AI) to process vast amounts of operational data in real time. This allows for more accurate predictions of fleet performance and potential issues (especially visible in railway transportation). Additionally, there is a growing focus on the use of cloud computing to store and analyze data, enabling scalable and flexible data management across entire fleets. The combination of edge computing with DTs is also becoming more prevalent, allowing for faster data processing and analysis at the source, which reduces latency and improves decision-making. Finally, the use of digital twins to create a unified data environment for the entire fleet enhances the ability to track and optimize individual vehicle performance as well as overall fleet efficiency.

Integration with management systems: A digital twin can be integrated with existing fleet and maintenance management systems, enabling automatic data transfer and collaboration between different platforms and applications. This helps streamline operations and improve data consistency and accessibility (see, e.g., ref. [

]). Leading trends include the seamless connection of DTs with enterprise resource planning (ERP) systems and computerized maintenance management systems (CMMSs). This integration allows for real-time data exchange and better synchronization of operational and maintenance activities. There is also a trend towards incorporating DTs with predictive maintenance systems, enabling automated decision-making based on real-time data analytics. Furthermore, the use of cloud-based platforms to unify DTs with various management systems is becoming more common, facilitating centralized control and easier scalability. Another emerging trend is the integration of DTs with Internet of Things (IoT) platforms, which enhances the capability to monitor and manage assets across distributed locations.

Safety and regulatory compliance: Implementing a DT in technical maintenance management requires addressing issues related to data security and compliance with regulatory requirements, such as data protection and occupational safety standards. Ensuring appropriate data protection measures and regulation compliance is crucial for successfully implementing the DT (e.g., refs. [

]). Leading trends here include using DTs to simulate and assess compliance with safety standards in real time, which helps identify potential hazards before they become critical. There is also a growing trend toward integrating DTs with automated compliance monitoring systems, enabling continuous oversight of regulatory requirements. Adopting DTs to create virtual testing environments is another trend, allowing for organizations to conduct safety drills and regulatory audits without disrupting actual operations. Additionally, DTs are increasingly being used to document and track regulatory compliance over the lifecycle of an asset, ensuring that all changes and updates are consistently managed and recorded.

The conducted systematic analysis of the selected literature makes it possible to answer the second research question.

RQ2 intended to define the main research and knowledge gaps in DT use in transportation systems operation and maintenance, especially in the context of in-house logistics. The main research outputs in this application area are discussed broadly in

. Internal logistics is vital for enhancing organizational productivity and operational efficiency, involving various activities related to material flow management. Digital twin (DT) applications in this domain include mobile robots, automated guided vehicles (AGVs), and decision support tools for logistics operations. Research covers DT architectures, real-time data streaming, and predictive maintenance for mobile robots and AGVs. Additionally, DT frameworks optimize warehouse management, monitor air quality, and improve safety. Overall, the integration of DTs in internal logistics presents opportunities for innovation and efficiency gains. Indeed, in the realm of digital twin (DT) application in internal logistics, warehousing, and autonomous transportation, several knowledge and research gaps have emerged that warrant further exploration.

One prominent challenge in the field of digital twin (DT) technology is the integration of these systems with existing logistics frameworks. Although numerous studies have explored various architectural approaches for DT implementation, there is a notable absence of comprehensive frameworks that address integration challenges across diverse logistics platforms. This research gap presents an opportunity to develop best practices and guidelines for seamlessly incorporating DT technology into existing logistics systems. Research could focus on identifying and standardizing integration strategies that accommodate the variability in current logistics infrastructures, ensuring interoperability and enhancing overall system efficiency. Furthermore, the effective handling of real-time data processing within DT systems remains a significant area of concern. While some studies have addressed real-time data streaming, there is insufficient understanding of how to maintain data integrity, security, and reliability, particularly in dynamic and variable environments. This gap emphasizes the need for research into robust real-time data management methodologies. Specifically, research should explore techniques for ensuring accurate and secure data transmission, processing, and storage in scenarios involving mobile and autonomous systems where decisions are highly time-sensitive. Investigations into advanced data management solutions that can handle the complexities of real-time data in logistics and other high-stakes environments will be crucial for advancing the practical application of DT technology.

Standardization also emerges as a significant issue within the DT landscape. The development of a standardized DT framework tailored to logistics operations, including mobile robots and AGVs, is yet to be comprehensively addressed. Future research could focus on creating standardized protocols and methodologies for designing and implementing DT technology across various logistics applications, ensuring consistency and interoperability.

While the potential of DTs in predictive maintenance is recognized, gaps still exist in understanding the limitations of predictive models in varying operational contexts. Future research should focus on quantifying the reliability of predictive analytics and evaluating their performance in different logistics environments. This would help refine the application of DTs for preemptive maintenance and enhance its overall effectiveness.

Another critical area of research pertains to the scalability of DT solutions. The current literature does not adequately document how to effectively scale DT applications from small to large operations without compromising their performance. Investigating scalable models would significantly contribute to the practical implementation of DTs across diverse logistics environments. Indeed, research into scalable models is needed to facilitate the widespread adoption of DT technologies across diverse logistics settings.

User interaction and training represent notable knowledge gaps in the implementation of digital twin (DT) technologies. There is a need for a deeper understanding of how users interact with DT systems to ensure they can effectively leverage these technologies. Additionally, developing effective training programs for less experienced operators is crucial to maximize the benefits of DT systems. Future research should focus on designing intuitive user interfaces that facilitate seamless interaction with DT technologies and creating comprehensive training methodologies. These efforts will support users in making informed decisions based on DT insights, ultimately enhancing the overall utility and effectiveness of digital twin applications.

Interoperability issues between different logistics platforms and systems represent a significant challenge in the implementation of digital twin (DT) technologies. Currently, there is a notable lack of comprehensive research addressing these interoperability challenges. Research should focus on developing methods and frameworks that facilitate seamless communication and data exchange across diverse DT systems. Addressing these gaps is essential for creating a more integrated logistics ecosystem where various platforms and systems can work together efficiently. This research is crucial for enhancing logistics operations’ overall effectiveness and cohesion, ensuring that DT technologies can deliver their full potential across different environments and applications.

Furthermore, the impact of external factors, such as economic conditions, supply chain disruptions, or changes in consumer behavior, on DT performance has not been thoroughly investigated. Gaining insight into these external influences would enhance the robustness and adaptability of DT models in real-world logistics applications.

Regulatory compliance is another critical area that requires further exploration. There is currently limited research on designing digital twin (DT) applications that adhere to regulatory standards in logistics and transportation. Specifically, more studies are needed to address how DT technologies can comply with data protection regulations and operational safety requirements. Investigating these aspects is essential for promoting the responsible and effective implementation of DT technologies. Ensuring that DT systems meet regulatory standards will help safeguard data integrity, enhance safety, and facilitate broader adoption of these technologies within the logistics and transportation sectors.

Cross-disciplinary approaches integrating insights from fields such as artificial intelligence and machine learning into DT applications in logistics remain underexplored. Investigating how these technologies can enhance the capabilities of DTs could lead to innovative solutions and improved operational efficiency. There is a notable gap in understanding how AI and machine learning can be effectively combined with DT to optimize processes, predict maintenance needs, and enhance decision-making. Addressing this gap could unlock new potential for DT systems, making them more robust and versatile in handling complex logistics challenges.

Finally, the environmental impact of implementing digital twin (DT) technologies in logistics is an area that warrants further exploration. Currently, there is limited research on how DTs can be utilized to enhance sustainability practices in warehousing and transportation. This gap in knowledge highlights the need for studies that investigate how DTs can contribute to reducing environmental impacts and improving resource efficiency. Addressing these research gaps is crucial for advancing the effective implementation and optimization of DT technologies, ensuring they support sustainable practices in internal logistics, warehousing, and autonomous transportation systems. By focusing on this aspect, future research can help integrate environmental considerations into the design and deployment of DT solutions, promoting a greener logistics industry.

By addressing these knowledge and research gaps, future studies could contribute to effectively implementing and optimizing digital twin technologies in internal logistics, warehousing, and autonomous transportation systems.

RQ3 intended to discover the main aspects of DT modeling to address future challenges in the operation and maintenance of transportation systems.

Despite the evident development of modern technologies and their application in the transport industry observed over the past five years, there remains significant potential for further advancements in the area of transport maintenance. Numerous aspects can be innovated, covering both technological and organizational solutions in relation to DT concept implementation. Currently, key development directions include the following:

Predictive diagnostics: The advancement of sophisticated diagnostic systems based on artificial intelligence and data analysis enables forecasting failures in advance. This allows for planning maintenance activities before problems arise, minimizing downtime and repair costs. Main developmental trends in this area include the application of advanced machine learning algorithms. Utilizing techniques such as regression algorithms, neural networks, and decision trees allows for more accurate data analysis and identifying patterns and anomalies that may indicate potential failures. Consequently, this enhances the precision of forecasting future technical issues.

Another widely analyzed area today is the integration with vehicle monitoring systems. Predictive diagnostics can be effectively utilized in conjunction with systems that monitor the technical condition of vehicles (e.g., AGVs, mobile robots). By integrating data from various sources, such as sensors, telemetry systems, or service databases, it is possible to obtain a comprehensive picture of the technical condition of the transport fleet. Modern solutions are also moving toward ensuring two-way communication between vehicles and servers.

An essential element of predictive diagnostics is optimizing the data collection, storage, and processing processes. It is crucial to focus on key technical parameters and factors influencing vehicle reliability to obtain the most relevant information for failure forecasting. Solutions based on blockchain technology and cloud-based systems will be increasingly important in this area in the near future. Moreover, the storage of vast quantities of data poses its own challenges. Efficient and scalable data storage solutions are necessary to manage the increasing volume of data generated by predictive diagnostics systems. Traditional storage methods may not be sufficient to handle the data’s scale and complexity, necessitating the development of more advanced and adaptable storage solutions.

Automation of maintenance processes is the next research area where we may identify research gaps. Implementing robotics and automation in maintenance processes can yield numerous benefits, including improved efficiency, task execution accuracy, and elimination of human errors. Robots can be employed to perform routine maintenance tasks, allowing for staff to focus on more advanced responsibilities. The main development direction in this area is using robots, drones, and automated devices to carry out routine tasks such as mechanical inspections, cleaning, or even minor repairs.

Blockchain technology is emerging as a promising solution for ensuring data integrity and security. By providing a decentralized and tamper-proof ledger, blockchain can enhance the reliability of data used in predictive diagnostics, ensuring that it remains accurate and unaltered throughout its lifecycle.

Cloud-based systems are also becoming increasingly important in managing and processing data for predictive diagnostics. The scalability and flexibility of cloud computing enable the handling of large volumes of data and the deployment of advanced analytics tools. Additionally, cloud-based solutions can facilitate real-time data access and collaboration among stakeholders, improving the efficiency and effectiveness of predictive diagnostics.

Another trend is the implementation of advanced decision support systems based on artificial intelligence and data analysis, which allow for optimizing the planning and execution of maintenance activities. These systems can suggest optimal schedules for inspections and repairs, considering priorities, costs, and resource availability. Automating technical inspections can expedite their execution and enhance their accuracy. Employing advanced technologies like vision systems and measuring devices facilitates rapid and precise assessment of vehicle conditions, making identifying problems and planning repair actions easier. In this context, there is a search for new solutions for “smart maintenance” and proactive maintenance approaches.

Integrated inventory management: Utilizing IoT technologies and warehouse management systems allows for better monitoring and optimizing spare parts and consumables inventory levels. This helps avoid material shortages during repairs and reduces costs associated with excess inventory. The next step in building integrated inventory management systems after implementing RFID (radio-frequency identification) technology is the introduction of inventory consumption monitoring systems. RFID technologies enable precise tracking of the location and condition of spare parts in warehouses. This facilitates the quick location of needed parts and minimizes the risk of material shortages during inspections and repairs. Consumption monitoring systems allow for continuous tracking of the technical condition of parts and forecasting replacement needs, enabling preemptive maintenance actions and inventory optimization, thereby reducing fleet maintenance costs.

There is also a trend in this area toward integrating inventory management systems with diagnostic systems and implementing IoT technologies, allowing for the automatic generation of spare parts orders based on the technical condition of vehicles. This enables swift responses to alarm signals and minimizes downtime due to material shortages.

The next research area is connected with mobile technologies and remote support. The development of mobile applications and remote technical support systems allows for quick diagnosis of problems and provision of repair instructions from anywhere, increasing the efficiency of maintenance activities and reducing vehicle downtime. The foundation of today’s proactive maintenance systems is the use of mobile applications by service personnel. This grants service staff quick access to essential data, operational instructions, and repair plans. These applications can also facilitate reporting failures, logging work hours, and communicating with team members, thereby enhancing operational efficiency.

The next step involves designing and implementing remote technical support systems, enabling rapid remote diagnosis of issues and providing repair guidance from specialists regardless of location. Utilizing tools like videoconferencing and remote access to diagnostic systems allows for effective problem resolution even for vehicles located far away. Additionally, there is a growing trend towards employing augmented and virtual reality technologies to assist personnel during the execution of basic operational tasks and in training programs. This facilitates continuous skill enhancement and tailors training to individual needs and abilities.

Implementing a digital twin technology allows for simulating and monitoring vehicle behavior in real-time, leading to a better understanding of operational processes and identifying areas for improvement. In the design and implementation of fleet management systems, primary development directions will focus on developing optimization and forecasting models to minimize costs and enhance the operational efficiency of transport systems. Furthermore, literature reviews and practical implementations indicate the necessity of developing solutions that allow for inter-departmental collaboration and data integration. Implementing a digital twin requires cooperation among different departments within a company and integration of data from various information systems. With appropriate technological solutions, it is possible to obtain a comprehensive view of the technical condition of the fleet and effectively coordinate maintenance activities at all levels of the organization.

Simultaneously, fundamental innovations regarding the design and implementation of the DT concept for ensuring the reliability and maintainability of internal transport systems will encompass the following:

Technological innovations—transport companies will introduce new technologies, such as AI, robotics, the Internet of Things, AR, and VR, with a DT approach to improve the efficiency and reliability of maintenance processes.

Organizational innovations—aimed at introducing new management methods, work procedures, or business models (e.g., robot as a service), which enable more efficient resource utilization and enhance the effectiveness of maintenance activities.

Process innovations—focused on optimizing existing maintenance processes and introducing new strategies and tools that allow for quicker responses to changes in operational conditions and minimize the risk of failures.

In conclusion, several fundamental limitations and challenges must be considered when developing and implementing the DT approach for maintaining technical systems, including the following:

Technical diagnostic issues: the necessity of monitoring and collecting significant amounts of information and processing this information for proper reporting.

Investment costs: Implementing modern technologies requires substantial financial investment, which will become evident through minimized repair and vehicle downtime costs due to better planning and resource utilization. The issue of investment profitability may limit companies.

Data security in collection and transmission processes: ensuring the security of transmitted data and minimizing the risk of cyberattacks are key aspects to consider when implementing Industry 4.0 technologies.

The conducted systematic analysis of the selected literature makes it possible to answer the last research question.

RQ4 intended to define the framework’s scope for digital twins in the maintenance management of transportation systems.

According to the literature review, defining a framework’s scope for digital twins (DTs) in the maintenance management of transportation systems should involve outlining objectives, key components, and functionalities that facilitate effective management and optimization of transportation assets. This review encompassed a wide range of research and case studies from different domains such as aviation, rail, road, and maritime transportation. By analyzing these diverse sources, we identified key trends, challenges, and best practices relevant to the implementation of DT technologies. This gives the possibility to define the main scope of the proposed framework.

The need for this framework to be grounded in the existing literature while tailored for internal transportation arises from the complexity and specificity of internal logistics operations. Although the general principles and technologies discussed in the literature apply across different transportation modes, the framework adapts these principles to meet the particular needs of internal transport environments.

First, the objectives of the digital twin framework for maintenance management in transportation systems should focus on enhancing asset reliability and operational efficiency through innovative technologies. Real-time monitoring allows for continuous assessment of asset conditions, facilitating immediate detection of anomalies and issues. Predictive maintenance leverages advanced analytics to foresee potential failures, enabling proactive actions that minimize downtime and associated costs. Performance optimization enhances operational efficiencies by providing actionable insights that guide data-driven decision-making processes.

Additionally, the framework supports simulation and testing, allowing for virtual experimentation with various maintenance strategies. This capability enables organizations to evaluate the effectiveness of different approaches without disrupting actual operations, leading to improved maintenance practices.

The key components of the DT framework include the following:

Data acquisition and integration: This component involves collecting real-time data from various sources, including sensors, IoT devices, and existing management systems. It is crucial for creating a comprehensive digital representation of physical assets, as it enables aggregating relevant data such as operational conditions, maintenance history, and environmental factors. Effective integration of these diverse data streams ensures that the digital twin remains accurate and reflects the system’s status.

Data analytics and visualization: Once the data are collected, advanced analytics techniques, including machine learning and statistical analysis, are employed to derive insights. This component helps identify data patterns, trends, and anomalies, facilitating predictive maintenance and decision-making. Visualization tools play a critical role in presenting complex data in a user-friendly manner, enabling stakeholders to interpret findings and make informed decisions easily.

Simulation and modeling: This aspect of the framework allows for creating of virtual models that replicate the behavior of physical assets under various conditions. Through simulation, organizations can test different maintenance scenarios, evaluate the impact of potential changes, and optimize maintenance schedules. This capability not only aids in risk assessment but also supports strategic planning and resource allocation.

Communication and collaboration tools: Effective communication among stakeholders is essential for successfully implementing the digital twin framework. Collaborative tools enable seamless information sharing, ensuring that all team members, from maintenance personnel to management, are aligned and informed about asset status and maintenance activities.

Feedback mechanisms: A vital component of the digital twin framework is the establishment of feedback loops that facilitate continuous improvement. By analyzing the outcomes of maintenance actions and comparing them with the predictions made by the digital twin, organizations can refine their models and improve their predictive capabilities, leading to more effective maintenance strategies over time.

Together, these components create a robust framework that enhances the maintenance management of transportation systems, ultimately leading to increased operational efficiency, reduced costs, and improved asset longevity. In addition, these key components should be reflected in the physical and virtual layers of the DT.

The last issue is connected with DT framework functionalities. In this area, we may distinguish six main functionalities:

Condition monitoring—providing dashboards and alerts that reflect the real-time health status of assets, allowing for immediate action when anomalies are detected.

Failure prediction—implementing predictive algorithms that analyze historical and real-time data to forecast potential failures and recommend maintenance actions accordingly.

Maintenance scheduling—automatically generating and optimizing maintenance schedules based on predicted failure points, historical maintenance data, and operational requirements.

Resource management—helping manage spare parts inventory and resource allocation by predicting the demand for parts based on the analysis of maintenance schedules.

Reporting and compliance—facilitating reporting functionalities to ensure compliance with regulatory requirements and standards in maintenance practices.

Feedback loop—establishing a feedback mechanism to continuously improve the digital twin models and algorithms based on actual maintenance outcomes and operational experiences.

The digital twin framework for maintenance management in transportation systems should represent a transformative approach to enhancing asset performance, optimizing maintenance strategies, and ensuring operational efficiency. As organizations increasingly adopt digital transformation strategies, integrating the digital twin framework with existing systems becomes crucial for maximizing its potential and ensuring a seamless transition.

In summary, successfully implementing the digital twin framework for maintenance management in transportation systems hinges on effective integration with existing systems and a commitment to future scalability and adaptability. Organizations can enhance their maintenance strategies and operational efficiency by creating a cohesive ecosystem that leverages historical data and encourages cross-departmental collaboration. Moreover, by designing the framework with flexibility in mind, organizations can ensure that the digital twin continues to meet their evolving needs, driving long-term asset performance and reliability improvements. This forward-thinking approach positions organizations to thrive in an increasingly complex and dynamic transportation landscape.

6. Framework for DTs in Transportation System Maintenance Management

The development of the framework presented in this study is a direct outcome of an extensive literature review conducted in the area of digital twin (DT) applications for transportation systems. Through a thorough examination of existing research and technological advancements, we identified key trends, challenges, and best practices relevant to the use of DTs in the operation and maintenance of transportation systems. This comprehensive review allowed for us to distill the core elements and principles necessary for creating an effective framework that addresses the common needs and objectives across different transportation domains.

The literature review highlights the growing importance of implementing digital twins (DTs) in the maintenance management of internal logistics systems, particularly internal transportation systems. In the context of effective maintenance management, DT technology plays a significant role, as it enables the evolution of maintenance strategies. Additionally, it enhances technical systems’ reliability, efficiency, and safety. Consequently, this article proposes conceptual frameworks for DTs as a tool to support key activities related to physical asset management. It presents conceptual frameworks for DTs in maintaining internal transportation systems.

], conceptual frameworks for DTs are presented, which include two interworking areas: the physical system and the virtual space. According to this standard, the conceptual frameworks consist of three main layers of the model in the virtual part and a connected layer in the real area (

The main layers of the DT model based on ISO 23247. Source: own contribution.

Based on ISO 23247, a conceptual framework for DTs in the maintenance of internal transportation systems can be proposed (

The conceptual framework for DTs in transportation systems. Source: own contribution.

The proposed conceptual framework’s first level (OE) pertains to the physical system. This includes all elements belonging to the internal transport system. Therefore, this layer encompasses not only the infrastructure of the space and its fixed elements (e.g., transport devices, storage racks) but also monitors the flow of goods and environmental conditions. These elements are continuously monitored using various measuring devices. The data collected from the OE layer form the basis for creating the virtual part of the digital twin, which is an exact replica of the real system.

Data obtained from the real system are collected and analyzed in the communication unit (Level II). This unit effectively communicates between the physical elements and their digital twin or directly with the user unit. Two subunits are distinguished in this area: the data collection subunit and the device control subunit. Data collected from the observed elements are transmitted to the digital twin unit to update the real system’s virtual copy continuously. Additionally, these data can be directly transferred to the user unit. The device control subunit controls and activates OE elements in response to requests from the user or DT units. This communication link between the real system, the user unit, and the DT unit enables the entire system to operate in two modes:

Fully automated mode, where a closed-loop connection exists between the communication unit and the DT unit;

Semi-automated mode, where feedback with instructions comes directly from the user unit.

The conceptual framework’s main component is the digital twin unit (Level III). Here, a virtual model of the internal transport system is developed based on data collected from Level I. This model reflects the real state and behavior of each system element. It is systematically updated based on newly collected data to ensure consistency with the actual state of the system. Additionally, this area includes a cache that stores current and historical information about each element of the real system.

The next level, Level IV—the user unit—is designed to enable employees to manage the digital twin and facilitate interpreting results generated by the DT unit. The main tasks in this area include defining maintenance goals and tasks, collecting maintenance data, and generating task commands. This unit contains functions that allow for monitoring of the OE and its digital twin and systems responsible for simulation, forecasting, data analysis, and reporting. Additionally, the user can support maintenance decision-making from this level, allowing for the system to operate in semi-automated mode. The user layer should also allow for integration with other systems and tools, enabling information exchange between different platforms.

The proposed conceptual framework also includes a cross-system entity that facilitates communication between all units in the system. Data transmitted and received must be recorded in a language understandable to the communicating units. Intermediary systems are used to translate communication protocols between different units to ensure uniform data. Additionally, integration platforms are used to facilitate data flow and state synchronization between the real system and the digital twin. This intermediary unit also includes systems responsible for supporting data security.

While the framework is grounded in the theoretical foundations and established principles from the literature, its practical implementation requires detailed consideration of specific steps and technical aspects. The framework consists of several interconnected layers and components, each playing a critical role in optimizing DT applications for internal transportation systems, and each should be carefully implemented based on the following implementation steps and technical details:

Implementation steps: Begin by identifying and cataloging all physical elements within the internal transportation system, including transport devices, storage racks, and environmental sensors. Implement continuous monitoring using advanced measuring devices to collect real-time data on asset performance and environmental conditions.

Technical details: Deploy IoT sensors and actuators for data acquisition, ensuring they are capable of interfacing with the data collection infrastructure. Integrate these data into a centralized database for further processing.

Implementation steps: Establish a robust data communication framework to facilitate the transfer of information between physical elements and their digital counterparts. Develop and integrate subunits for data collection and device control.

Technical Details: Utilize cloud-based systems and blockchain technology to ensure data integrity and security during transmission. Implement middleware solutions to bridge communication protocols between diverse systems.

Implementation steps: Create a virtual model of the internal transport system using the data collected from Level I. This virtual model should be dynamically updated to reflect the real-time state and behavior of the physical system.

Technical details: Implement simulation software and data analytics tools to process and visualize the data. Ensure the model includes a data cache for storing current and historical information to support predictive maintenance and performance analysis.

Implementation steps: Design intuitive user interfaces that allow for operators to interact with the digital twin, define maintenance tasks, and manage system operations. Provide functionalities for data analysis, simulation, and reporting.

Technical details: Develop user-friendly dashboards and decision support tools to facilitate effective management of the digital twin. Integrate the user unit with other enterprise systems to enable seamless information exchange and support semi-automated operations.

Implementation steps: develop and implement integration platforms and intermediary systems to ensure consistent communication and data exchange between different units within the system.

Technical details: Use standardized data formats and protocols to ensure uniformity across the system. Incorporate data security measures to protect against unauthorized access and ensure compliance with regulatory standards.

In summary, the framework draws from established theoretical foundations and the existing literature on DTs, ensuring it aligns with the core principles and trends identified in scholarly research. For instance, it incorporates the DT concept as defined by ISO 23247 [

], which outlines a structured approach with interworking areas including the physical system and the virtual space. This adherence to theoretical standards ensures that the framework is grounded in established research while being adaptable to practical applications in internal transportation systems.

In addition to theoretical integration, the framework is designed to complement asset management concepts. It incorporates essential elements of asset management, such as the continuous monitoring and evaluation of physical assets, the use of data for predictive maintenance, and the optimization of maintenance strategies. By doing so, it aligns with the broader asset management framework, enhancing the reliability, efficiency, and safety of internal transportation systems. This alignment underscores the framework’s role in advancing asset management practices through the application of DT technologies.

The development of this framework also directly addresses several identified research gaps in the literature. For example, current literature indicates a lack of standardized protocols for implementing DTs across various domains. Our framework proposes standardized approaches and methodologies for designing and implementing DT systems, ensuring consistency and interoperability within internal transportation systems.

In addition, the challenge of scaling DT solutions from small-scale implementations to large operations is a significant gap. Our framework addresses this by providing scalable models that ensure performance is maintained across diverse operational scales.

Understanding user interactions with DT systems and designing effective training programs are crucial for maximizing technology benefits. The framework includes provisions for user-friendly interfaces and comprehensive training methodologies to support effective decision-making.

The framework tackles interoperability issues by creating methods for seamless communication and data exchange between different DT systems, fostering a more integrated logistics ecosystem.

By addressing these gaps, the framework not only builds upon the insights and standards established in the literature but also advances the practical application of DT technologies in internal transportation systems. It serves as a comprehensive tool that bridges theoretical principles with practical asset management needs, thereby contributing to the effective implementation and optimization of digital twin technologies in diverse logistical contexts.

This article presents a systematic literature review addressing the main areas of digital twin utilization in the operation and maintenance of transportation systems. The analysis of 201 recent publications from 2012 to 2024, along with a review of publication trends, allowed for a discussion of specific applications of DT in the transportation sector.

The presented work suffers several limitations, mostly related to the reviewing methodology assumptions connected with publication collection, searching strategy, and filtering criteria. Here, the most notable limitation is associated with the used keywords as a search engine. Despite using a broad spectrum of keywords, some works connected with transportation sector O&M processes may be omitted. Indeed, despite efforts to cover a broad range of terminology related to DTs, variations in terminology across different fields or research groups may lead to gaps in capturing all relevant aspects of DTs. In addition, the literature related to medicine, health issues, or environmental aspects is omitted in the conducted overview analysis. The authors focused on logistics, transportation, and supply chain-related publications. Moreover, the conducted literature analysis does not consider the quality of the investigated publications based on times cited. The authors present only the most cited keywords in their bibliometric analyses. Another limitation may be connected with the geographical scope of the reviewed studies. A majority of the sources come from China, which may potentially restrict the global applicability of the results. What should also be underlined is that the authors focused on publications like peer-reviewed articles and conference papers, possibly overlooking significant research found in industry reports, white papers, or theses that might provide additional insights into digital twin (DT) applications. The last aspect is connected with the comparability of the selected publications. The diversity in methodologies across the reviewed studies could impact the comparability of results and affect the general conclusions drawn about the effectiveness and application of DTs.

The systematic literature review identified seven fundamental research areas within the transportation sector where the use of DTs for maintenance has been analyzed. The conducted literature review highlighted several key findings. One of the most important is that modern service and maintenance methods, along with the role of digital twins, are key factors in ensuring transportation fleets’ durability, maintainability, and reliability. Adapting to the changing technological landscape and fostering collaboration among various stakeholders in the industry are essential for further improving fleet service and maintenance processes. Continued discussion and cooperation can contribute to introducing innovative solutions to ensure a safe and efficient transportation infrastructure for future generations.

The authors’ future research direction may involve addressing the challenges that could arise when implementing a digital twin framework in internal transportation systems within real enterprises. Additionally, future steps should include exploring potential issues related to integrating such frameworks, such as interoperability, data security, and the need for standardization across different systems.

The authors recommend a more exhaustive literature review for future work, especially related to domain-specific areas. Furthermore, topics such as sustainable maintenance systems or mitigating environmental impacts related to new technology implementation may require further exploration. Another interesting research direction may be connected with developing a new business model. In this area, concepts such as “Machine as a Service” or “Software as a Service” are other trends suitable for future research.

The authors would like to thank the reviewers for their insightful comments.

The following abbreviations are used in this manuscript:

Developing digital twin systems with automated model management

Preferred Reporting Items for Systematic Reviews and Meta-Analyzes

The following supporting information can be downloaded at:

https://www.mdpi.com/article/10.3390/s24186069/s1

Conceptualization, S.W.-W. and R.G.; methodology, S.W.-W., R.G. and K.W.; formal analysis, S.W.-W., R.G. and K.W.; resources, S.W.-W., R.G. and K.W.; data curation, S.W.-W., R.G. and K.W.; writing—original draft preparation, S.W.-W., R.G. and K.W.; writing—review and editing, S.W.-W., R.G. and K.W.; visualization, S.W.-W., R.G. and K.W.; supervision, S.W.-W. All authors have read and agreed to the published version of the manuscript.

The authors declare no conflicts of interest.

This research received no external funding.

The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.

Cockerell B.S. Is the Transportation Industry Ready for Digital Twins? 2022. [(accessed on 1 July 2024)]. Available online:

https://www.bentley.com/wp-content/uploads/industry-trends-digital-twins-in-rail-stevecockerell.pdf

Kartsan P., Mavrin S. The Digital Revolution of the Transportation Industry. Transp. Res. Procedia. 2023;68:116–119. doi: 10.1016/j.trpro.2023.02.014.

Ammar A., Maier F., Pratt W.S., Richard E., Dadi G. Practical Application of Digital Twins for Transportation Asset Data Management: Case Example of a Safety Hardware Asset. Transp. Res. Rec. 2024 doi: 10.1177/03611981241231804.

Tubis A.A., Poturaj H., Smok A. Interaction between a Human and an AGV System in a Shared Workspace—A Literature Review Identifying Research Areas. Sustainability. 2024;16:974. doi: 10.3390/su16030974.

Astarita V., Guido G., Haghshenas S.S., Haghshenas S.S. Risk Reduction in Transportation Systems: The Role of Digital Twins According to a Bibliometric-Based Literature Review. Sustainability. 2024;16:3212. doi: 10.3390/su16083212.

Ersöz O.Ö., İnal A.F., Aktepe A., Türker A.K., Ersöz S. A Systematic Literature Review of the Predictive Maintenance from Transportation Systems Aspect. Sustainability. 2022;14:14536. doi: 10.3390/su142114536.

Alawaysheh I., Alsyouf I. Environmental Sustainability in Maintenance Management of Public Transport Systems: Literature Review. IEEE Int. Conf. Ind. Eng. Eng. Manag. 2018:1125–1129. doi: 10.1109/IEEM.2018.8607535.

Bernal E., Spiryagin M., Cole C. Onboard Condition Monitoring Sensors, Systems and Techniques for Freight Railway Vehicles: A Review. IEEE Sens. J. 2019;19:4–24. doi: 10.1109/JSEN.2018.2875160.

Brant J., Liang B. Condition Monitoring Systems in the Railway Industry BT—Advances in Asset Management and Condition Monitoring. In: Ball A., Gelman L., Rao B.K.N., editors. Advances in Asset Management and Condition Monitoring. Smart Innovation, Systems and Technologies, Vol. 166. Springer International Publishing; Cham, Switzerland: 2020. pp. 671–683.

De Donato L., Flammini F., Marrone S., Mazzariello C., Nardone R., Sansone C., Vittorini V. A Survey on Audio-Video Based Defect Detection Through Deep Learning in Railway Maintenance. IEEE Access. 2022;10:65376–65400. doi: 10.1109/ACCESS.2022.3183102.

Entezami M., Roberts C., Weston P., Stewart E., Amini A., Papaelias M. Perspectives on Railway Axle Bearing Condition Monitoring. Proc. Inst. Mech. Eng. Part F J. Rail Rapid Transit. 2019;234:17–31. doi: 10.1177/0954409719831822.

Fraga-Lamas P., Fernández-Caramés T.M., Castedo L. Towards the Internet of Smart Trains: A Review on Industrial IoT-Connected Railways. Sensors. 2017;17:1457. doi: 10.3390/s17061457.

Sitarz M., Chruzik K. An Approach to the Legal Requirements Regarding Railway Transport Safety Monitoring in the European Union. Transport. 2019;34:163–174. doi: 10.3846/transport.2019.8528.

Chen Y., Li Y., Niu G., Zuo M. Offline and Online Measurement of the Geometries of Train Wheelsets: A Review. IEEE Trans. Instrum. Meas. 2022;71:1–15. doi: 10.1109/TIM.2022.3205691.

Gogu C. Prognostics and Health Management: Current State-of-the-Art for Optimizing Aircraft Structural Maintenance; Proceedings of the 2018 19th International Conference on Thermal, Mechanical and Multi-Physics Simulation and Experiments in Microelectronics and Microsystems (EuroSimE); Toulouse, France. 15–18 April 2018; pp. 1–4.

Meijer M. Preventive Maintenance of Transport Vehicles Is It Improving Production Stability of a Smelter? BT—Light Metals 2013. In: Sadler B.A., editor. Proceedings of the Light Metals 2013. The Minerals, Metals & Materials Series. Springer International Publishing; Berlin/Heidelberg, Germany: 2016. pp. 669–671.

Hou Y., Li Q., Zhang C., Lu G., Ye Z., Chen Y., Wang L., Cao D. The State-of-the-Art Review on Applications of Intrusive Sensing, Image Processing Techniques, and Machine Learning Methods in Pavement Monitoring and Analysis. Engineering. 2021;7:845–856. doi: 10.1016/j.eng.2020.07.030.

Wieczorek A., Stecuła K., Wes Grebski W. Methods and Techniques Supporting Energy and Media Savings in Maintenance of Public Transport Buses—State of the Art and Recommendations. Energies. 2024;17:2051. doi: 10.3390/en17092051.

Choudhary A., Fatima S., Panigrahi B.K. State-of-the-Art Technologies in Fault Diagnosis of Electric Vehicles: A Component-Based Review. IEEE Trans. Transp. Electrif. 2023;9:2324–2347. doi: 10.1109/TTE.2022.3209166.

Knowles M., Ren Q., Baglee D. The State of the Art in Fuel Cell Condition Monitoring and Maintenance; Proceedings of the EVS 2010—Sustainable Mobility Revolution: 25th World Battery, Hybrid and Fuel Cell Electric Vehicle Symposium and Exhibition; Shenzhen, China. 5–8 November 2010; pp. 487–494.

Gbako S., Paraskevadakis D., Ren J., Wang J., Radmilovic Z. A Systematic Literature Review of Technological Developments and Challenges for Inland Waterways Freight Transport in Intermodal Supply Chain Management. Benchmarking. 2024.

Negi P., Kromanis R., Dorée A.G., Wijnberg K.M. Structural Health Monitoring of Inland Navigation Structures and Ports: A Review on Developments and Challenges. Struct. Heal. Monit. 2024;23:605–645. doi: 10.1177/14759217231170742.

Allaix D.L., Bigaj-Van Vliet A., Cerar B. Review of the Current State of Standardisation on Monitoring, Data-Informed Safety Assessment and Decision-Making Regarding Maintenance of the Transport Infrastructure; Proceedings of the IABSE Symposium: Challenges for Existing and Oncoming Structures; Prague, Czech Republic. 25–27 May 2022;

Cepa J.J., Pavón R.M., Alberti M.G., Ciccone A., Asprone D. A Review on the Implementation of the BIM Methodology in the Operation Maintenance and Transport Infrastructure. Appl. Sci. 2023;13:3176. doi: 10.3390/app13053176.

Hoelzl C., Dertimanis V., Landgraf M., Ancu L., Zurkirchen M., Chatzi E. On-Board Monitoring for Smart Assessment of Railway Infrastructure: A Systematic Review. Rise Smart Cities Adv. Struct. Sens. Monit. Syst. 2022:223–259. doi: 10.1016/B978-0-12-817784-6.00015-1.

Komalan N. Aggregation and Fault Detection Techniques for Tracks Using Wireless Sensor Network; Proceedings of the International Conference on Innovative Mechanisms for Industry Applications (ICIMIA 2017); Bengaluru, India. 21–23 February 2017; pp. 116–123.

Ngamkhanong C., Kaewunruen S., Afonso Costa B.J. State-of-the-Art Review of Railway Track Resilience Monitoring. Infrastructures. 2018;3:3. doi: 10.3390/infrastructures3010003.

Taheri A., Sobanjo J. Civil Integrated Management (CIM) for Advanced Level Applications to Transportation Infrastructure: A State-of-the-Art Review. Infrastructures. 2024;9:90. doi: 10.3390/infrastructures9060090.

Zinno R., Haghshenas S.S., Guido G., Vitale A. Artificial Intelligence and Structural Health Monitoring of Bridges: A Review of the State-of-the-Art. IEEE Access. 2022;10:88058–88078. doi: 10.1109/ACCESS.2022.3199443.

Tubis A.A., Rohman J. Intelligent Warehouse in Industry 4.0—Systematic Literature Review. Sensors. 2023;23:4105. doi: 10.3390/s23084105.

Selvam K., Dhiman H.S., Pandya D., Sahoo S. Synergizing Digital Twins for Enhanced Maintenance of Integrated Chargers in Electric Vehicles: A State-of-the-Art Analysis and Future Implications; Proceedings of the 2023 International Conference on Integration of Computational Intelligent System (ICICIS); Pune, India. 1–4 November 2023; pp. 1–6.

Page M.J., McKenzie J.E., Bossuyt P.M., Boutron I., Hoffmann T.C., Mulrow C.D., Shamseer L., Tetzlaff J.M., Akl E.A., Brennan S.E., et al. The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews. BMJ. 2021;372:71. doi: 10.1136/bmj.n71.

Vohra M. Overview of Digital Twin. In: Vohra M., editor. Digital Twin Technology: Fundamentals and Applications. Scrivener Publishing LLC; Beverly, MA, USA: 2023. pp. 1–18.

Singh M., Fuenmayor E., Hinchy E.P., Qiao Y., Murray N., Devine D. Digital Twin: Origin to Future. Appl. Syst. Innov. 2021;4:36. doi: 10.3390/asi4020036.

Boyes H., Watson T. Digital Twins: An Analysis Framework and Open Issues. Comput. Ind. 2022;143:103763. doi: 10.1016/j.compind.2022.103763.

Sharma A., Kosasih E., Zhang J., Brintrup A., Calinescu A. Digital Twins: State of the Art Theory and Practice, Challenges, and Open Research Questions. J. Ind. Inf. Integr. 2022;30:100383. doi: 10.1016/j.jii.2022.100383.

Matyi H., Tamás P. Application of Digital Twin Technology in the Development of Logistics Process. Adv. Logist. Syst. Theory Pract. 2021;15:12–19. doi: 10.32971/als.2021.002.

Barricelli B.R., Casiraghi E., Fogli D. A Survey on Digital Twin: Definitions, Characteristics, Applications, and Design Implications. IEEE Access. 2019;7:167653–167671. doi: 10.1109/ACCESS.2019.2953499.

Digital Twin: Definition & Value. AIAA; Reston, VA, USA: 2020. An AIAA and AIA Position Paper.

Fang X., Wang H., Liu G., Tian X., Ding G., Zhang H. Industry Application of Digital Twin: From Concept to Implementation. Int. J. Adv. Manuf. Technol. 2022;121:4289–4312. doi: 10.1007/s00170-022-09632-z.

van Beek A., Nevile Karkaria V., Chen W. Digital Twins for the Designs of Systems: A Perspective. Struct. Multidiscip. Optim. 2023;66:1–17. doi: 10.1007/s00158-023-03488-x.

Jones D., Snider C., Nassehi A., Yon J., Hicks B. Characterising the Digital Twin: A Systematic Literature Review. CIRP J. Manuf. Sci. Technol. 2020;29:36–52. doi: 10.1016/j.cirpj.2020.02.002.

Schwartz S.M., Wildenhaus K., Bucher A., Byrd B. Digital Twins and the Emerging Science of Self: Implications for Digital Health Experience Design and “Small” Data. Front. Comput. Sci. 2020;2:1–16. doi: 10.3389/fcomp.2020.00031.

Rasheed A., San O., Kvamsdal T. Digital Twin: Values, Challenges and Enablers from a Modeling Perspective. IEEE Access. 2020;8:21980–22012. doi: 10.1109/ACCESS.2020.2970143.

Agrawal A., Fischer M., Singh V. Digital Twin: From Concept to Practice. J. Manag. Eng. 2022;38 doi: 10.1061/(ASCE)ME.1943-5479.0001034.

Harper K.E., Ganz C., Harper K.E. Digital Twin Architecture and Standards. IIC J. Innov. 2019;2019:1–12.

van der Valk H., Haße H., Möller F., Otto B. Archetypes of Digital Twins. Bus. Inf. Syst. Eng. 2022;64:375–391. doi: 10.1007/s12599-021-00727-7.

Rathore M.M., Shah S.A., Shukla D., Bentafat E., Bakiras S. The Role of AI, Machine Learning, and Big Data in Digital Twinning: A Systematic Literature Review, Challenges, and Opportunities. IEEE Access. 2021;9:32030–32052. doi: 10.1109/ACCESS.2021.3060863.

Minerva R., Lee G.M., Crespi N. Digital Twin in the IoT Context: A Survey on Technical Features, Scenarios, and Architectural Models. Proc. IEEE. 2020;108:1785–1824. doi: 10.1109/JPROC.2020.2998530.

Lv Z. Digital Twins in Industry 5.0. Research. 2023;6:1–16. doi: 10.34133/research.0071.

Tao F., Qi Q., Wang L., Nee A.Y.C. Digital Twins and Cyber–Physical Systems toward Smart Manufacturing and Industry 4.0: Correlation and Comparison. Engineering. 2019;5:653–661. doi: 10.1016/j.eng.2019.01.014.

Fett M., Turner E., Breimann R., Kirchner E. Extension of the System Boundary of the Digital Twin onto the Sensors of the Physical Twin through the Introduction of Redundant Soft Sensors. Forsch. Im Ingenieurwesen/Eng. Res. 2023;87:479–488. doi: 10.1007/s10010-023-00653-y.

Xu Y., Kohtz S., Boakye J., Gardoni P., Wang P. Physics-Informed Machine Learning for Reliability and Systems Safety Applications: State of the Art and Challenges. Reliab. Eng. Syst. Saf. 2023;230:108900. doi: 10.1016/j.ress.2022.108900.

Röhm B., Emich B., Anderl R. Approach of Simulation Data Management for the Application of the Digital Simulation Twin. Procedia CIRP. 2021;100:421–426. doi: 10.1016/j.procir.2021.05.098.

Bestjak L., Lindqvist C. M.Sc. Thesis. School of Innovation, Design and Engineering, Malardalens Hogskola Eskilstuna Vasteras; Vasteras, Sweden: 2020. Assessment of How Digital Twin Can Be Utilized in Manufacturing Companies to Create Business Value.

Grieves M., Vickers J. Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems. In: Kahlen F.J., Flumerfelt S., Alves A., editors. Transdisciplinary Perspectives on Complex Systems: New Findings and Approaches. Springer International Publishing; Chem, Switzerland: 2017. pp. 85–113.

Jones D.E., Snider C., Kent L., Hicks B. Early Stage Digital Twins for Early Stage Engineering Design. Proc. Int. Conf. Eng. Des. ICED. 2019;1:2557–2566. doi: 10.1017/dsi.2019.262.

Schluse M., Rossmann J. From Simulation to Experimentable Digital Twins: Simulation-Based Development and Operation of Complex Technical Systems; Proceedings of the 2016 IEEE International Symposium on Systems Engineering (ISSE); Edinburgh, UK. 3–5 October 2016; pp. 1–6.

Wang K., Wang Y., Li Y., Fan X., Xiao S., Hu L. A Review of the Technology Standards for Enabling Digital Twin. Digit. Twin. 2022;2:4. doi: 10.12688/digitaltwin.17549.1.

Botín-Sanabria D.M., Mihaita S., Peimbert-García R.E., Ramírez-Moreno M.A., Ramírez-Mendoza R.A., Lozoya-Santos J.D.J. Digital Twin Technology Challenges and Applications: A Comprehensive Review. Remote Sens. 2022;14:1335. doi: 10.3390/rs14061335.

Ozkaya I. Architectural Concerns of Digital Twins. IEEE Softw. 2022;39:3–6. doi: 10.1109/MS.2021.3130872.

Radanliev P., De Roure D., Nicolescu R., Huth M., Santos O. Digital Twins: Artificial Intelligence and the IoT Cyber-Physical Systems in Industry 4.0. Int. J. Intell. Robot. Appl. 2022;6:171–185. doi: 10.1007/s41315-021-00180-5.

Balogh M., Földvári A., Varga P. Digital Twins in Industry 5.0: Challenges in Modeling and Communication; Proceedings of the IEEE/IFIP Network Operations and Management Symposium 2023, NOMS 2023; Miami, FL, USA. 8–12 May 2023.

Wang B., Zhou H., Li X., Yang G., Zheng P., Song C., Yuan Y., Wuest T., Yang H., Wang L. Human Digital Twin in the Context of Industry 5.0. Robot. Comput. Integr. Manuf. 2024;85:102626. doi: 10.1016/j.rcim.2023.102626.

Eleftheriou O.T., Anagnostopoulos C.-N. Digital Twins: A Brief Overview of Applications, Challenges and Enabling Technologies in the Last Decade. Digit. Twin. 2022;2:2. doi: 10.12688/digitaltwin.17581.1.

Alnowaiser K.K., Ahmed M.A. Digital Twin: Current Research Trends and Future Directions. Arab. J. Sci. Eng. 2023;48:1075–1095. doi: 10.1007/s13369-022-07459-0.

Hribernik K., Cabri G., Mandreoli F., Mentzas G. Autonomous, Context-Aware, Adaptive Digital Twins—State of the Art and Roadmap. Comput. Ind. 2021;133:103508. doi: 10.1016/j.compind.2021.103508.

Hu W., Zhang T., Deng X., Liu Z., Tan J. Digital Twin: A State-of-the-Art Review of Its Enabling Technologies, Applications and Challenges. J. Intell. Manuf. Spec. Equip. 2021;2:1–34. doi: 10.1108/JIMSE-12-2020-010.

Kuehner K.J., Scheer R., Strassburger S. Digital Twin: Finding Common Ground—A Meta-Review. Procedia CIRP. 2021;104:1227–1232. doi: 10.1016/j.procir.2021.11.206.

Alcaraz C., Lopez J. Digital Twin: A Comprehensive Survey of Security Threats. IEEE Commun. Surv. Tutor. 2022;24:1475–1503. doi: 10.1109/COMST.2022.3171465.

Ji T., Huang H., Xu X. Digital Twin Technology—A Bibliometric Study of Top Research Articles Based on Local Citation Score. J. Manuf. Syst. 2022;64:390–408. doi: 10.1016/j.jmsy.2022.06.016.

Mihai S., Yaqoob M., Hung D.V., Davis W., Towakel P., Raza M., Karamanoglu M., Barn B., Shetve D., Prasad R.V., et al. Digital Twins: A Survey on Enabling Technologies, Challenges, Trends and Future Prospects. IEEE Commun. Surv. Tutor. 2022;24:2255–2291. doi: 10.1109/COMST.2022.3208773.

Rossmann A., Hertweck D. Digital Twins: A Meta-Review on Their Conceptualization, Application, and Reference Architecture; Proceedings of the 55th Hawaii International Conference on System Sciences; Maui, HI, USA. 4–7 January 2022; pp. 4518–4527.

Kitchenham B. Procedures for Performing Systematic Reviews. Keele University; Keele, UK: 2004. Joint technical report: Keele University Technical Report, TR/SE-0401 and NICTA Technical Report 040001IT.1.

Attaran M., Celik B.G. Digital Twin: Benefits, Use Cases, Challenges, and Opportunities. Decis. Anal. J. 2023;6:100165. doi: 10.1016/j.dajour.2023.100165.

Correia J.B., Abel M., Becker K. Data Management in Digital Twins: A Systematic Literature Review. Knowl. Inf. Syst. 2023;65:3165–3196. doi: 10.1007/s10115-023-01870-1.

Melesse T.Y., Di Pasquale V., Riemma S. Digital Twin Models in Industrial Operations: A Systematic Literature Review. Procedia Manuf. 2020;42:267–272. doi: 10.1016/j.promfg.2020.02.084.

Kitchenham B. Guidelines for Performing Systematic Literature Reviews in Software Engineering. School of Computer Science and Mathematics, Keele University & University of Durham; Durham, UK: 2007. EBSE Technical Report EBSE-2007-01.

Liu Y.K., Ong S.K., Nee A.Y.C. State-of-the-Art Survey on Digital Twin Implementations. Adv. Manuf. 2022;10:1–23. doi: 10.1007/s40436-021-00375-w.

Segovia M., Garcia-Alfaro J. Design, Modeling and Implementation of Digital Twins. Sensors. 2022;22:5396. doi: 10.3390/s22145396.

Perno M., Hvam L., Haug A. Implementation of Digital Twins in the Process Industry: A Systematic Literature Review of Enablers and Barriers. Comput. Ind. 2022;134:103558. doi: 10.1016/j.compind.2021.103558.

Xiong M., Wang H. Digital Twin Applications in Aviation Industry: A Review. Int. J. Adv. Manuf. Technol. 2022;121:5677–5692. doi: 10.1007/s00170-022-09717-9.

Ferko E., Bucaioni A., Behnam M. Architecting Digital Twins. IEEE Access. 2022;10:50335–50350. doi: 10.1109/ACCESS.2022.3172964.

Oliveira P.P. Digital Twin Development for Airport Management. J. Airpt. Manag. 2020;14:246–259. doi: 10.69554/PZMM9316.

Tao F., Zhang H., Liu A., Nee A.Y.C. Digital Twin in Industry: State-of-the-Art. IEEE Trans. Ind. Inform. 2019;15:2405–2415. doi: 10.1109/TII.2018.2873186.

Fu Y., Zhu G., Zhu M., Xuan F. Digital Twin for Integration of Design-Manufacturing-Maintenance: An Overview. Chin. J. Mech. Eng. 2022;35:80. doi: 10.1186/s10033-022-00760-x.

Moenck K., Rath J.E., Koch J., Wendt A., Kalscheuer F., Schüppstuhl T., Schoepflin D. Digital twins in aircraft production and MRO: Challenges and opportunities. CEAS Aeronaut. J. 2024 doi: 10.1007/s13272-024-00740-y.

Singh M., Srivastava R., Fuenmayor E., Kuts V., Qiao Y., Murray N., Devine D. Applications of Digital Twin across Industries: A Review. Appl. Sci. 2022;12:5727. doi: 10.3390/app12115727.

Rjabtšikov V., Rassõlkin A., Kudelina K., Kallaste A., Vaimann T. Review of Electric Vehicle Testing Procedures for Digital Twin Development: A Comprehensive Analysis. Energies. 2023;16:6952. doi: 10.3390/en16196952.

Piromalis D., Kantaros A. Digital Twins in the Automotive Industry: The Road toward Physical-Digital Convergence. Appl. Syst. Innov. 2022;5:65. doi: 10.3390/asi5040065.

Sharma M., George J.P. Digital Twin in the Automotive Industry : Driving Physical-Digital Convergence. Tata Consultancy Services; Mumbai, India: 2018. pp. 1–8. White Paper.

Vandana, Garg A., Panigrahi B.K. Multi-dimensional Digital Twin of Energy Storage System for Electric Vehicles: A Brief Review. Energy Storage. 2021;3:e242. doi: 10.1002/est2.242.

Naseri F., Gil S., Barbu C., Cetkin E., Yarimca G., Jensen A.C., Larsen P.G., Gomes C. Digital Twin of Electric Vehicle Battery Systems: Comprehensive Review of the Use Cases, Requirements, and Platforms. Renew. Sustain. Energy Rev. 2023;179:113280. doi: 10.1016/j.rser.2023.113280.

Elbazi N., Tigami A., Laayati O., El Maghraoui A., Chebak A., Mabrouki M. Digital Twin-Enabled Monitoring of Mining Haul Trucks with Expert System Integration: A Case Study in an Experimental Open-Pit Mine; Proceedings of the 2023 IEEE 5th Global Power, Energy and Communication Conference, GPECOM; Cappadocia, Turkiye. 14–16 June 2023; Piscataway, NJ, USA: IEEE; 2023. pp. 168–174.

Le T.V., Fan R. Digital Twins for Logistics and Supply Chain Systems: Literature Review, Conceptual Framework, Research Potential, and Practical Challenges. Comput. Ind. Eng. 2024;187:109768. doi: 10.1016/j.cie.2023.109768.

Moshood T.D., Nawanir G., Sorooshian S., Okfalisa O. Digital Twins Driven Supply Chain Visibility within Logistics: A New Paradigm for Future Logistics. Appl. Syst. Innov. 2021;4:29. doi: 10.3390/asi4020029.

Kosacka-Olejnik M., Kostrzewski M., Marczewska M., Mrówczyńska B., Pawlewski P. How Digital Twin Concept Supports Internal Transport Systems?—Literature Review. Energies. 2021;14:4919. doi: 10.3390/en14164919.

Nguyen T., Duong Q.H., Van Nguyen T., Zhu Y., Zhou L. Knowledge Mapping of Digital Twin and Physical Internet in Supply Chain Management: A Systematic Literature Review. Int. J. Prod. Econ. 2022;244:108381. doi: 10.1016/j.ijpe.2021.108381.

Ivanova T., Shkrobot M. Digitalization in the Reverse Supply Chain: A Bibliometric Analysis. Logforum. 2023;19:683–702. doi: 10.17270/J.LOG.2023.865.

Liu J., Yeoh W., Qu Y., Gao L. Blockchain-Based Digital Twin for Supply Chain Management: State-of-The-Art Review and Future Research Directions. SSRN Electron. J. 2022:1–34. doi: 10.2139/ssrn.4113933.

Bhandal R., Meriton R., Kavanagh R.E., Brown A. The Application of Digital Twin Technology in Operations and Supply Chain Management: A Bibliometric Review. Supply Chain Manag. 2022;27:182–206. doi: 10.1108/SCM-01-2021-0053.

Phanden R.K., Sharma P., Dubey A. A Review on Simulation in Digital Twin for Aerospace, Manufacturing and Robotics. Mater. Today Proc. 2020;38:174–178. doi: 10.1016/j.matpr.2020.06.446.

Baidya S., Das S.K., Uddin M.H., Kosek C., Summers C. Digital Twin in Safety-Critical Robotics Applications: Opportunities and Challenges; Proceedings of the 41st IEEE International Performance Computing and Communications Conference (IPCCC); Austin, TX, USA. 11–13 November 2022; pp. 101–107.

Waqar A., Othman I., Almujibah H., Khan M.B., Alotaibi S., Elhassan A.A.M. Factors Influencing Adoption of Digital Twin Advanced Technologies for Smart City Development: Evidence from Malaysia. Buildings. 2023;13:775. doi: 10.3390/buildings13030775.

Azeez N.A., Adjekpiyede O.O. Digital Twin Technology: A Review of Its Applications and Prominent Challenges. Covenant J. Inform. Commun. Technol. 2022;10:1–15.

Bado M.F., Tonelli D., Poli F., Zonta D., Casas J.R. Digital Twin for Civil Engineering Systems: An Exploratory Review for Distributed Sensing Updating. Sensors. 2022;22:3168. doi: 10.3390/s22093168.

Popa E.O., van Hilten M., Oosterkamp E., Bogaardt M.J. The Use of Digital Twins in Healthcare: Socio-Ethical Benefits and Socio-Ethical Risks. Life Sci. Soc. Policy. 2021;17:1–25. doi: 10.1186/s40504-021-00113-x.

Primo Egoavil X., Sucaticona Araujo F., De La Torre Salazar J. Viability of the Digital Twin in the Inventory of Educational Assets to Improve Maintenance Control; Proceedings of the 2022 Congreso Internacional de Innovación y Tendencias en Ingeniería (CONIITI); Bogota, Colombia. 5–7 October 2022; pp. 1–6.

Rassudov L., Akmurzin E., Korunets A., Osipov D. Engineering Education and Cloud-Based Digital Twins for Electric Power Drive System Diagnostics; Proceedings of the 2021 28th International Workshop on Electric Drives: Improving Reliability of Electric Drives, IWED 2021; Moscow, Russia. 27–29 January 2021.

Kairat K., Ildar P., Karygash A., Saule B., Indira K., Markhaba K., Aizhan B. Digital Twins Technology in the Educational Process of the Aviation Equipment Repair. Indones. J. Electr. Eng. Comput. Sci. 2023;32:752–762. doi: 10.11591/ijeecs.v32.i2.pp752-762.

Schneider G., Wendl M., Kucek S., Leitner M. A Training Concept Based on a Digital Twin for a Wafer Transportation System; Proceedings of the 2021 IEEE 23rd Conference on Business Informatics, CBI; Bolzano, Italy. 1–3 September 2021; Piscataway, NJ, USA: IEEE; 2021. pp. 20–28.

Gray A. The Routledge International Handbook of Embodied Perspectives in Psychotherapy. Routledge; London, UK: 2019. Body as Voice: Restorative Dance/Movement Psychotherapy with Survivors of Relational Trauma; pp. 147–160.

Dąbrowska A., Giel R., Winiarska K. Sequencing and Planning of Packaging Lines with Reliability and Digital Twin Concept Considerations—A Case Study of a Sugar Production Plant. Logforum. 2022;18:321–334. doi: 10.17270/J.LOG.2022.762.

You Y., Chen C., Hu F., Liu Y., Ji Z. Advances of Digital Twins for Predictive Maintenance. Procedia Comput. Sci. 2022;200:1471–1480. doi: 10.1016/j.procs.2022.01.348.

van Dinter R., Tekinerdogan B., Catal C. Predictive Maintenance Using Digital Twins: A Systematic Literature Review. Inf. Softw. Technol. 2022;151:107008. doi: 10.1016/j.infsof.2022.107008.

Zhong D., Xia Z., Zhu Y., Duan J. Overview of Predictive Maintenance Based on Digital Twin Technology. Heliyon. 2023;9:e14534. doi: 10.1016/j.heliyon.2023.e14534.

Booyse W., Wilke D.N., Heyns S. Deep Digital Twins for Detection, Diagnostics and Prognostics. Mech. Syst. Signal Process. 2020;140:106612. doi: 10.1016/j.ymssp.2019.106612.

Okeagu F.N., Mgbemena C.E. A Systematic Review of Digital Twin Systems for Improved Predictive Maintenance of Equipment in Smart Factories. Int. J. Ind. Prod. Eng. 2022;1:1–20.

Gosavi A., Le V.K. Maintenance Optimization in a Digital Twin for Industry 4.0. Ann. Oper. Res. 2024;340:245–269. doi: 10.1007/s10479-022-05089-1.

Agnusdei G.P., Elia V., Gnoni M.G. A Classification Proposal of Digital Twin Applications in the Safety Domain. Comput. Ind. Eng. 2021;154:107137. doi: 10.1016/j.cie.2021.107137.

Thorn A.C., Technology P.H.M., Conroy P., Technology P.H.M., Chan D., Technology P.H.M., Stecki C., Technology P.H.M. The Digital Risk Twin—Enabling Model-Based RAMS; Proceedings of the 2023 Annual Reliability and Maintainability Symposium (RAMS); Orlando, FL, USA. 23–26 January 2023; Piscataway, NJ, USA: IEEE; 2023. pp. 1–6.

Mohanraj E., Eniyavan N., Sidarth S., Sridharan S. Digital Twins for Automotive Predictive Maintenance; Proceedings of the 7th International Conference on Inventive Computation Technologies, ICICT 2024; Kathmandu, Nepal. 24–26 April 2024; pp. 1579–1584.

Hilton S., Technology P.H.M., Langton J., Technology P.H.M., Conroy P., Technology P.H.M., Stecki C., Technology P.H.M. Digital Availability Twin—Targeted Risk Mitigation from Design to Operation; Proceedings of the 2023 Annual Reliability and Maintainability Symposium (RAMS); Orlando, FL, USA. 23–26 January 2023; Piscataway, NJ, USA: IEEE; 2023. pp. 1–6.

Aivaliotis P., Georgoulias K., Alexopoulos K. Using Digital Twin for Maintenance Applications in Manufacturing: State of the Art and Gap Analysis; Proceedings of the 2019 IEEE International Conference on Engineering, Technology and Innovation (ICE/ITMC); Valbonne Sophia-Antipolis, France. 17–19 June 2019;

Errandonea I., Beltrán S., Arrizabalaga S. Digital Twin for Maintenance: A Literature Review. Comput. Ind. 2020;123:103316. doi: 10.1016/j.compind.2020.103316.

Ali W.A., Roccotelli M., Fanti M.P. Digital Twin in Intelligent Transportation Systems: A Review; Proceedings of the 2022 8th International Conference on Control, Decision and Information Technologies, CoDIT 2022; Istanbul, Turkey. 17–20 May 2022; pp. 576–581.

Irfan M.S., Dasgupta S., Rahman M. Towards Transportation Digital Twin Systems for Traffic Safety and Mobility Applications: A Review. arXiv. 20222212.12242

Munkeby S.K. M.Sc. Thesis. Norvegian University of Science and Technology; Trondheim, Norway: 2022. On Application of Digital Twin in Ship Operation and Performance.

Aita D. Digitization in Ports: Application of Digital Twins to Complex Logistics. FAL Bull. 2022;393

Saifutdinov F., Tolujevs J. Time and Space Discretization in the Digital Twin of the Airport Transport Network. Transp. Telecommun. 2021;22:257–265. doi: 10.2478/ttj-2021-0019.

Errandonea I., Goya J., Alvarado U., Beltron S., Arrizabalaga S. IoT Approach for Intelligent Data Acquisition for Enabling Digital Twins in the Railway Sector; Proceedings of the 2021 International Symposium on Computer Science and Intelligent Controls (ISCSIC); Rome, Italy. 12–14 November 2021; pp. 164–168.

Kampczyk A., Dybeł K. The Fundamental Approach of the Digital Twin Application in Railway Turnouts with Innovative Monitoring of Weather Conditions. Sensors. 2021;21:5757. doi: 10.3390/s21175757.

Pool A. M.Sc. Thesis. University of Twente; Enschede, Netherlands: 2021. Digital Twins in Rail Freight—The Foundations of a Future Innovation.

Dasgupta S., Rahman M., Lidbe A.D., Lu W., Jones S. A Transportation Digital-Twin Approach for Adaptive Traffic Control Systems. arXiv. 20212109.10863

Guo Y., Zou K., Chen S., Yuan F., Yu F. 3D Digital Twin of Intelligent Transportation System Based on Road-Side Sensing. J. Phys. Conf. Ser. 2021;2083:032022. doi: 10.1088/1742-6596/2083/3/032022.

Kušić K., Schumann R., Ivanjko E. A Digital Twin in Transportation: Real-Time Synergy of Traffic Data Streams and Simulation for Virtualizing Motorway Dynamics. Adv. Eng. Inform. 2023;55:101858. doi: 10.1016/j.aei.2022.101858.

Marcucci E., Gatta V., Le Pira M., Hansson L., Bråthen S. Digital Twins: A Critical Discussion on Their Potential for Supporting Policy-making and Planning in Urban Logistics. Sustainability. 2020;12:10623. doi: 10.3390/su122410623.

Rudskoy A., Ilin I., Prokhorov A. Digital Twins in the Intelligent Transport Systems. Transp. Res. Procedia. 2021;54:927–935. doi: 10.1016/j.trpro.2021.02.152.

Felix-Cigalat J.S., Domingo R. Towards a Digital Twin Warehouse through the Optimization of Internal Transport. Appl. Acoust. 2023;13:4652. doi: 10.3390/app13084652.

Ganesh M., Rizvi A.M., Anbu A. Digital Twin Framework for Material Handling and Logistics in Manufacturing: Part 1; Proceedings of the 2022 International Conference on Connected Systems & Intelligence (CSI); Trivandrum, India. 31 August–2 September 2022; Piscataway, NJ, USA: IEEE; 2022.

Martínez-Gutiérrez A., Díez-González J., Ferrero-Guillén R., Verde P., Álvarez R., Perez H. Digital Twin for Automatic Transportation in Industry 4.0. Sensors. 2021;21:3344. doi: 10.3390/s21103344.

Cruz H., Raheem A.A., Nazarian S. Digital Twin Technology Applications for Transportation Infrastructure—A Survey-Based Study. Comput. Civ. Eng. 2021;2021:350–357.

Vieira J., Martins J.P., de Almeida N.M., Patricio H. Towards Resilient and Sustainable Rail and Road Networks: A Systematic Literature Review on Digital Twins. Sustainability. 2022;14:7060. doi: 10.3390/su14127060.

Assani N., Matić P., Katalinić M. Ship’s Digital Twin—A Review of Modelling Challenges and Applications. Appl. Sci. 2022;12:6039. doi: 10.3390/app12126039.

Kaiblinger A., Woschank M. State of the Art and Future Directions of Digital Twins for Production Logistics: A Systematic Literature Review. Appl. Sci. 2022;12:669. doi: 10.3390/app12020669.

Gao C., Wang J., Dong S., Liu Z., Cui Z., Ma N., Zhao X. Application of Digital Twins and Building Information Modeling in the Digitization of Transportation: A Bibliometric Review. Appl. Sci. 2022;12:11203. doi: 10.3390/app122111203.

Budgen D., Brereton P. Performing Systematic Literature Reviews in Software Engineering. Proceedings of the ICSE ‘06, the 28th International Conference on Software Engineering, Shanghai, China, 20–21 May 2006. Volume 2006:1051–1052. doi: 10.1145/1134285.1134500.

Madhukar P., McCulloch M., Gorman J., Pai N.P., Enanoria W.T.A., Kennedy G.E., Tharyan P., Colford J.M. Systematic Reviews and Meta-Analyses: An Illustrated, Step-by-Step Guide. Natl. Med. J. India. 2004;17:86–95.

Zamani E.D., Smyth C., Gupta S., Dennehy D. Artificial Intelligence and Big Data Analytics for Supply Chain Resilience: A Systematic Literature Review. Ann. Oper. Res. 2022;327:605–632. doi: 10.1007/s10479-022-04983-y.

Aromataris E., Pearson A. The Systematic Review: An Overview. Am. J. Nurs. 2014;114:53–58. doi: 10.1097/01.NAJ.0000444496.24228.2c.

Tranfield D., Denyer D., Smart P. Towards a Methodology for Developing Evidence-Informed Management Knowledge by Means of Systematic Review. Br. J. Manag. 2003;14:207–222. doi: 10.1111/1467-8551.00375.

Moher D., Liberati A., Tetzlaff J., Altman D.G. Preferred Reporting Items for Systematic Reviews and Meta-Analyses: The PRISMA Statement. Int. J. Surg. 2010;8:336–341. doi: 10.1016/j.ijsu.2010.02.007.

Agrawal S., Oza P., Kakkar R., Tanwar S., Jetani V., Undhad J., Singh A. Analysis and Recommendation System-Based on PRISMA Checklist to Write Systematic Review. Assess. Writ. 2024;61:100866. doi: 10.1016/j.asw.2024.100866.

[(accessed on 1 June 2024)]. Available online:

https://Omnis-Pwr.Primo.Exlibrisgroup.Com/Discovery/Search?Vid=48OMNIS_TUR:48TUR&lang=pl&mode=advanced

Liu H., Xia M., Williams D., Sun J., Yan H. Digital Twin-Driven Machine Condition Monitoring: A Literature Review. J. Sensors. 2022;2022:1–13. doi: 10.1155/2022/6129995.

Werbińska-Wojciechowska S., Winiarska K. Maintenance Performance in the Age of Industry 4.0: A Bibliometric Performance Analysis and a Systematic Literature Review. Sensors. 2023;23:1409. doi: 10.3390/s23031409.

Welch V., Petticrew M., Petkovic J., Moher D., Waters E., White H., Tugwell P. Extending the PRISMA Statement to Equity-Focused Systematic Reviews (PRISMA-E 2012): Explanation and Elaboration. J. Clin. Epidemiol. 2016;70:68–89. doi: 10.1016/j.jclinepi.2015.09.001.

Prikler L.M., Wotawa F. A Systematic Mapping Study of Digital Twins for Diagnosis in Transportation; Proceedings of the 2023 10th International Conference on Dependable Systems and Their Applications, DSA 2023; Tokyo, Japan. 10–11 August 2023; pp. 431–442.

Yan B., Yang F., Qiu S., Wang J., Cai B., Wang S., Zaheer Q., Wang W., Chen Y., Hu W. Digital Twin in Transportation Infrastructure Management: A Systematic Review. Intell. Transp. Infrastruct. 2023;2:liad024. doi: 10.1093/iti/liad024.

Watson R.T., Webster J. Analysing the Past to Prepare for the Future: Writing a Literature Review a Roadmap for Release 2.0. J. Decis. Syst. 2020;29:129–147. doi: 10.1080/12460125.2020.1798591.

Wang J., Li X., Wang P., Liu Q. Bibliometric Analysis of Digital Twin Literature: A Review of Influencing Factors and Conceptual Structure. Technol. Anal. Strateg. Manag. 2024;36:166–180. doi: 10.1080/09537325.2022.2026320.

Krüger S., Borsato M. Developing Knowledge on Digital Manufacturing to Digital Twin: A Bibliometric and Systemic Analysis. Procedia Manuf. 2019;38:1174–1180. doi: 10.1016/j.promfg.2020.01.207.

Agnusdei G.P., Elia V., Gnoni M.G. Is Digital Twin Technology Supporting Safety Management? A Bibliometric and Systematic Review. Appl. Sci. 2021;11:2767. doi: 10.3390/app11062767.

Lorenzetti D.L., Ghali W.A. Reference Management Software for Systematic Reviews and Meta-Analyses: An Exploration of Usage and Usability. BMC Med. Res. Methodol. 2013;13:141. doi: 10.1186/1471-2288-13-141.

da Silva A.A., Pedrosa M.R. Using Reference Manager (Mendeley) in Systematic Reviews. Cochrane Brasil; São Paulo, Brazil: 2018.

VOSviewer. [(accessed on 15 June 2024)]. Available online:

van Eck N.J., Waltman L. Software Survey: VOSviewer, a Computer Program for Bibliometric Mapping. Scientometrics. 2010;84:523–538. doi: 10.1007/s11192-009-0146-3.

Bernal E., Wu Q., Spiryagin M., Cole C. Augmented Digital Twin for Railway Systems Augmented Digital Twin for Railway Systems. Veh. Syst. Dyn. 2023;62:67–83. doi: 10.1080/00423114.2023.2194543.

Bernal E., Spiryagin M., Vollebregt E., Oldknow K., Stichel S., Shrestha S., Ahmad S., Wu Q., Sun Y., Cole C. Prediction of Rail Surface Damage in Locomotive Traction Operations Using Laboratory-Field Measured and Calibrated Data. Eng. Fail. Anal. 2022;135:106165. doi: 10.1016/j.engfailanal.2022.106165.

Ahmad S., Spiryagin M., Wu Q., Bernal E., Sun Y., Cole C., Makin B. Development of a Digital Twin for Prediction of Rail Surface Damage in Heavy Haul Railway Operations. Veh. Syst. Dyn. 2023;62:41–66. doi: 10.1080/00423114.2023.2237620.

Spiryagin M., Edelmann J., Klinger F., Cole C. Vehicle System Dynamics in Digital Twin Studies in Rail and Road Domains. Veh. Syst. Dyn. 2023;61:1737–1786. doi: 10.1080/00423114.2023.2188228.

Guo Y., Zhu Q., Ding Y., Li Y., Wu H., He Y., Li Z., Li H., Zhang L., Zhao Y., et al. Efficient Distributed Association Management Method of Data, Model, and Knowledge for Digital Twin Railway. Int. J. Digit. Earth. 2024;17:2340089. doi: 10.1080/17538947.2024.2340089.

Li L., Aslam S., Wileman A., Perinpanayagam S. Digital Twin in Aerospace Industry: A Gentle Introduction. IEEE Access. 2022;10:9543–9562. doi: 10.1109/ACCESS.2021.3136458.

Liao M., Renaud G., Bombardier Y. Airframe Digital Twin Technology Adaptability Assessment and Technology Demonstration. Eng. Fract. Mech. 2020;225:106793. doi: 10.1016/j.engfracmech.2019.106793.

Li J., Zhou G., Zhang C. A Twin Data and Knowledge-Driven Intelligent Process Planning Framework of Aviation Parts. Int. J. Prod. Res. 2022;60:5217–5234. doi: 10.1080/00207543.2021.1951869.

Borgo M.D., Elliott S.J., Ghandchi M., Ian T. Virtual Sensing of Wheel Direction from Redundant Sensors in Aircraft Ground—Steering Systems. CEAS Aeronaut. J. 2022;13:199–213. doi: 10.1007/s13272-021-00557-z.

Mhenni F., Vitolo F., Rega A., Plateaux R., Hehenberger P., Patalano S., Choley J. Heterogeneous Models Integration for Safety Critical Mechatronic Systems and Related Digital Twin Definition: Application to a Collaborative Workplace for Aircraft Assembly. Appl. Sci. 2022;12:2787. doi: 10.3390/app12062787.

Apostolidis A., Stamoulis K.P. An AI-Based Digital Twin Case Study in the MRO Sector. Transp. Res. Procedia. 2021;56:55–62. doi: 10.1016/j.trpro.2021.09.007.

Smagin D.I., Grachev S.V., Suchkov M.V., Vereikin A.A. Method for Predictive Analysis of Failure and Pre-Failure Conditions of Aircraft Units Using Data Obtained during Their Operation. Aerosp. Syst. 2023;6:231–248. doi: 10.1007/s42401-022-00178-2.

Zaccaria V., Stenfelt M., Aslanidou I., Kyprianidis K.G. Fleet Monitoring and Diagnostics Framework Based on Digital Twin of Aero-Engines; Proceedings of the ASME Turbo Expo American Society of Mechanical Engineers (ASME); Oslo, Norway. 11–15 June 2018; pp. 1–10.

Xiong M., Wang H., Fu Q., Xu Y. Digital Twin—Driven Aero-Engine Intelligent Predictive Maintenance. Int. J. Adv. Manuf. Technol. 2021;114:3751–3761. doi: 10.1007/s00170-021-06976-w.

Wu Z., Li J. A Framework of Dynamic Data Driven Digital Twin for Complex Engineering Products: The Example of Aircraft Engine Health Management. Procedia Manuf. 2021;55:139–146. doi: 10.1016/j.promfg.2021.10.020.

Ren J., Cheng Y., Zhang Y., Tao F. A Digital Twin-Enhanced Collaborative Maintenance Paradigm for Aero-Engine Fleet. Front. Eng. Manag. 2024;11:356–361. doi: 10.1007/s42524-024-0299-z.

Wang Z., Wang Y., Wang X., Yang K., Zhao Y. A Novel Digital Twin Framework for Aeroengine Performance Diagnosis. Aerospace. 2023;10:789. doi: 10.3390/aerospace10090789.

Kilic U., Yalin G., Cam O. Digital Twin for Electronic Centralized Aircraft Monitoring by Machine Learning Algorithms. Energy. 2023;283:129118. doi: 10.1016/j.energy.2023.129118.

Ezhilarasu C.M., Jennions I.K. A System-Level Failure Propagation Detectability Using ANFIS for an Aircraft Electrical Power System. Appl. Sci. 2020;10:2854. doi: 10.3390/app10082854.

Starostin I.E., Khalyutin S.P., Druzhinin A.A., Gavrilenkov S.I. Development of an Information System of Digital Twins of Aviation Electrical Equipment as a Software Module of the Local Load Control Center; Proceedings of the 2023 20th Technical Scientific Conference on Aviation Dedicated to the Memory of N.E. Zhukovsky, TSCZh 2023; Moscow, Russia. 13–14 April 2023; Piscataway, NJ, USA: IEEE; 2023. pp. 26–31.

Liu W., Li X., Shen Z., Ma C. A Digital Twin Method for Civil Aircraft Power Distribution System Based on Unity3D and Simulink. J. Phys. Conf. Ser. 2023;2615:012017. doi: 10.1088/1742-6596/2615/1/012017.

Ren B., Gao Y., Gu Z., Liu P., Xiong J. Intelligent Equipment Scenario for Aviation Maintenance VR System Based on Digital Twin Model; Proceedings of the 2024 5th International Conference on Mobile Computing and Sustainable Informatics, ICMCSI 2024; Lalitpur, Nepal. 18–19 January 2024; Piscataway, NJ, USA: IEEE; 2024. pp. 427–433.

Utzig S., Kaps R., Azeem S.M., Gerndt A. Augmented Reality for Remote Collaboration in Aircraft Maintenance Tasks; Proceedings of the 2019 IEEE Aerospace Conference; Big Sky, MT, USA. 2–9 March 2019; Piscataway, NJ, USA: IEEE; 2019. pp. 1–10.

Wei R., Yang R., Liu S., Fan C., Zhou R., Wu Z., Wang H., Cai Y., Jiang Z. Towards an Extensible Model-Based Digital Twin Framework for Space Launch Vehicles. J. Ind. Inf. Integr. 2024;41:100641. doi: 10.1016/j.jii.2024.100641.

Wu M., Xiao Y., Gao Y., Xiao M. Digital Twin for UAV-RIS Assisted Vehicular Communication Systems. IEEE Trans. Wirel. Commun. 2023;23:7638–7651. doi: 10.1109/TWC.2023.3342991.

Tavares S.M.O., Ribeiro J.A., Ribeiro B.A., de Castro P.M.S.T. Aircraft Structural Design and Life-Cycle Assessment through Digital Twins. Designs. 2024;8:29. doi: 10.3390/designs8020029.

Sadeghi A., Bellavista P., Song W., Yazdani-Asrami M. Digital Twins for Condition and Fleet Monitoring of Aircraft: Towards More-Intelligent Electrified Aviation Systems. IEEE Access. 2024;12:99806–99832. doi: 10.1109/ACCESS.2024.3371902.

Bisanti G.M., Mainetti L., Montanaro T., Patrono L., Sergi I. Digital Twins for Aircraft Maintenance and Operation: A Systematic Literature Review and an IoT-Enabled Modular Architecture. Internet Things. 2023;24:100991. doi: 10.1016/j.iot.2023.100991.

Goraj R. Digital Twin of the Rotor-Shaft of a Lightweight Electric Motor during Aerobatics Loads. Aircr. Eng. Aerosp. Technol. 2020;92:1319–1326. doi: 10.1108/AEAT-11-2019-0231.

Oyekan J., Farnsworth M., Hutabarat W., Miller D. Applying a 6 DoF Robotic Arm and Digital Twin to Automate Fan-Blade Reconditioning for Aerospace Maintenance, Repair, and Overhaul. Sensors. 2020;20:4637. doi: 10.3390/s20164637.

Millwater H., Ocampo J., Crosby N. Probabilistic Methods for Risk Assessment of Airframe Digital Twin Structures. Eng. Fract. Mech. 2019;221:106674. doi: 10.1016/j.engfracmech.2019.106674.

Pinello L., Hassan O., Giglio M., Sbarufatti C. Preliminary Nose Landing Gear Digital Twin for Damage Detection. Aerospace. 2024;11:222. doi: 10.3390/aerospace11030222.

Ezhilarasu C.M., Skaf Z., Jennions I.A.N.K. A Generalised Methodology for the Diagnosis of Aircraft Systems. IEEE Access. 2021;9:11437–11454. doi: 10.1109/ACCESS.2021.3050877.

Dong Y., Jiang H., Wu Z., Yang Q., Liu Y. Digital Twin-Assisted Multiscale Residual-Self-Attention Feature Fusion Network for Hypersonic Flight Vehicle Fault Diagnosis. Reliab. Eng. Syst. Saf. 2023;235:109253. doi: 10.1016/j.ress.2023.109253.

Seshadri B.R., Krishnamurthy T. Structural Health Management of Damaged Aircraft Structures Using the Digital Twin Concept; Proceedings of the 25th AIAA/AHS Adaptive Structures Conference; Grapevine, TX, USA. 9–13 January 2017; pp. 1–13.

Heim S., Clemens J., Steck J.E., Basic C. Predictive Maintenance on Aircraft and Applications with Digital Twin; Proceedings of the 2020 IEEE International Conference on Big Data (Big Data); Atlanta, GA, USA. 10–13 December 2020; pp. 4122–4127.

Ho G.T.S., Ming Y., Yat K., Tang V., Yin K. A Blockchain-Based System to Enhance Aircraft Parts Traceability and Trackability for Inventory Management. Expert Syst. Appl. 2021;179:115101. doi: 10.1016/j.eswa.2021.115101.

Winkler P., Gallego-Garcia S., Groten M. Design and Simulation of a Digital Twin Mobility Concept: An Electric Aviation System Dynamics Case Study with Capacity Constraints. Appl. Sci. 2022;12:848. doi: 10.3390/app12020848.

Shen G., Lei L., Li Z., Cai S., Zhang L., Cao P., Liu X. Deep Reinforcement Learning for Flocking Motion of Multi-UAV Systems: Learn From a Digital Twin. IEEE Internet Things J. 2022;9:11141–11153. doi: 10.1109/JIOT.2021.3127873.

Dimitrova E., Tomov S. Digital Twins: An Advanced Technology for Railways Maintenance Transformation; Proceedings of the 2021 13th Electrical Engineering Faculty Conference (BulEF); Varna, Bulgaria. 8–11 September 2021; Piscataway, NJ, USA: IEEE; 2021. pp. 1–5.

Ikeda M. Recent Research and Development Activities in Maintenance Technologies for Electric Railway Power Supply Systems. Q. Rep. RTRI. 2020;61:1–5. doi: 10.2219/rtriqr.61.1_6.

Vatakov V., Pencheva E., Dimitrova E. Recent Advances in Artificial Intelligence for Improving Railway Operations; Proceedings of the 30th National Conference with International Participation “Telecom 2022”; Sofia, Bulgaria. 27–28 October 2022; Piscataway, NJ, USA: IEEE; 2022. pp. 7–10.

Dirnfeld R., De Donato L., Somma A., Azari M.S., Marrone S., Flammini F., Vittorini V. Integrating AI and DTs: Challenges and Opportunities in Railway Maintenance Application and Beyond. Simulation. 2024;100:903–917. doi: 10.1177/00375497241229756.

Ghaboura S., Ferdousi R., Laamarti F., Yang C., Saddik A. El Digital Twin for Railway: A Comprehensive Survey. IEEE Access. 2023;11:120237–120257. doi: 10.1109/ACCESS.2023.3327042.

Zhang T., Du W., Zhang G., Wang J. PHM of Rail Vehicle Based on Digital Twin; Proceedings of the 2021 Global Reliability and Prognostics and Health Management (PHM-Nanjing); Nanjing, China. 15–17 October 2021; pp. 1–5.

Guillén López A.J., Gómez Fernández J.F., Urda P., Escalona J.L., Crespo Márquez A., Olivencia F. Digital Twin for Condition Based Maintenance within a Railway Infrastructure Testing Lab; Proceedings of the PHM Society Asia-Pacific Conference; Tokyo, Japan. 11–14 September 2023; pp. 1–7.

Putra H.G.P., Supangkat S.H., Nugraha I.G.B.B., Hidayat F. Designing Machine Learning Model for Predictive Maintenance of Railway Vehicle; Proceedings of the 2021 International Conference on ICT for Smart Society (ICISS); Bandung, Indonesia. 2–4 August 2021; Piscataway, NJ, USA: IEEE; 2021. pp. 1–5.

Jung C., Toguyeni A.K.A., Bouamama B.O. Supervised Machine Learning from Digital Twin Data for Railway Switch Fault Diagnosis; Proceedings of the 2023 European Control Conference, ECC 2023; Bucharest, Romania. 13–16 June 2023; pp. 1–7.

Bosso N., Magelli M., Trinchero R., Zampieri N. Application of Machine Learning Techniques to Build Digital Twins for Long Train Dynamics Simulations. Veh. Syst. Dyn. 2023;62:21–40. doi: 10.1080/00423114.2023.2174885.

Gálvez A., Rubio J., Seneviratne D., Gonzalez A., Jimenez A., Martinez-de-estarrona U., Galar D., Juuso E. Hybrid Models and Digital Twins for Condition Monitoring: HVAC System for Railway. SNE Tech. Note. 2021;31:121–126. doi: 10.11128/sne.31.tn.10572.

Bustos A., Rubio H., Soriano-Heras E., Castejon C. Methodology for the Integration of a High-Speed Train in Maintenance 4.0. J. Comput. Des. Eng. 2021;8:1605–1621. doi: 10.1093/jcde/qwab064.

Franzen J., Stecken J., Pfaff R., Kuhlenkötter B. Using the Digital Shadow for a Prescriptive Optimization of Maintenance and Operation. In: Clausen U., Langkau S., Kreuz F., editors. Advances in Production, Logistics and Traffic. ICPLT 2019. Lecture Notes in Logistics. Volume 1. Springer; Cham, Switzerland: 2019. pp. 265–276.

Guan K., Guo X., He D., Svoboda P., Berbineau M., Wang S., Ai B., Zhong Z., Rupp M. Key Technologies for Wireless Network Digital Twin towards Smart Railways. High Speed Railw. 2024;2:1–10. doi: 10.1016/j.hspr.2024.01.004.

Galvez A., Seneviratne D., Galar D. Hybrid Model Development for HVAC System in Transportation. Technologies. 2021;9:18. doi: 10.3390/technologies9010018.

H-Nia S., Flodin J., Casanueva C., Asplund M., Stichel S. Predictive Maintenance in Railway Systems: MBS- Based Wheel and Rail Life Prediction Exemplified for the Swedish Iron-Ore Line. Veh. Syst. Dyn. 2023;62:3–20. doi: 10.1080/00423114.2022.2161920.

Granzner M., Strauss A., Reiterer M., Cao M., Novák D. Data-Driven Condition Assessment and Life Cycle Analysis Methods for Dynamically and Fatigue-Loaded Railway Infrastructure Components. Infrastructures. 2023;8:162. doi: 10.3390/infrastructures8110162.

Rahman M., Liu H., Masri M., Durazo-cardenas I., Starr A. Computers in Industry A Railway Track Reconstruction Method Using Robotic Vision on a Mobile Manipulator: A Proposed Strategy. Comput. Ind. 2023;148:103900. doi: 10.1016/j.compind.2023.103900.

Pillai N., Shih J.-Y., Roberts C. Evaluation of Numerical Simulation Approaches for Simulating Train—Track Interactions and Predicting Rail Damage in Railway Switches and Crossings (S&Cs) Infrastructures. 2021;6:63. doi: 10.3390/infrastructures6050063.

Ramatlo D.A., Wilke D.N., Loveday P.W. Digital Twin Hybrid Modeling for Enhancing Guided Wave Ultrasound Inspection Signals in Welded Rails. Math. Comput. Appl. 2023;28:58. doi: 10.3390/mca28020058.

Zhang S., Dong H., Maschek U., Song H. A Digital-Twin-Assisted Fault Diagnosis of Railway Point Machine; Proceedings of the 2021 IEEE 1st International Conference on Digital Twins and Parallel Intelligence (DTPI); Beijing, China. 15 July–15 August 2021; Piscataway, NJ, USA: IEEE; 2021. pp. 430–433.

Yang J., Sun Y., Cao Y., Hu X. Predictive Maintenance for Switch Machine Based on Digital Twins. Information. 2021;12:485. doi: 10.3390/info12110485.

Kaewunruen S., Lian Q. Digital Twin Aided Sustainability-Based Lifecycle Management for Railway Turnout Systems. J. Clean. Prod. 2019;228:1537–1551. doi: 10.1016/j.jclepro.2019.04.156.

Sresakoolchai J., Kaewunruen S. Railway Infrastructure Maintenance Efficiency Improvement Using Deep Reinforcement Learning Integrated with Digital Twin Based on Track Geometry and Component Defects. Sci. Rep. 2023;13:2439. doi: 10.1038/s41598-023-29526-8.

Du W., Zhang T., Zhang G., Wang J. A Digital Twin Framework and an Implementaion Method for Urban Rail Transit; Proceedings of the 2021 Global Reliability and Prognostics and Health Management (PHM-Nanjing); Nanjing, China. 15–17 October 2021.

Doubell G.D., Basson A.H., Kruger K., Conradie P.D.F. A Digital Twin System for Railway Infrastructure. R&D J. 2023;39:23–34. doi: 10.17159/2309-8988/2023/v39a3.

Kim M., Hwang D., Park D. Analysis of Maintenance Techniques for a Three-Dimensional Digital Twin-Based Railway Facility with Tunnels. Platforms. 2023;1:5–17. doi: 10.3390/platforms1010002.

De Donato L., Dirnfeld R., Somma A., De Benedictis A., Flammini F., Marrone S., Saman Azari M., Vittorini V. Towards AI-Assisted Digital Twins for Smart Railways: Preliminary Guideline and Reference Architecture. J. Reliab. Intell. Environ. 2023;9:303–317. doi: 10.1007/s40860-023-00208-6.

Chen R., Jin C., Zhang Y., Dai J., Lv X. Digital Twin for Equipment Management of Intelligent Railway Station; Proceedings of the 2021 IEEE 1st International Conference on Digital Twins and Parallel Intelligence (DTPI); Beijing, China. 15 July–15 August 2021; Piscataway, NJ, USA: IEEE; 2021. pp. 374–377.

Chandaluri R., Nelakuditi U.R. Performance Evaluation of Electro-Mechanical Railway Interlocking System for Digital Twin Application. Comput. Electr. Eng. 2024;116:109225. doi: 10.1016/j.compeleceng.2024.109225.

Armijo A., Zamora-Sánchez D. Integration of Railway Bridge Structural Health Monitoring into the Internet of Things with a Digital Twin: A Case Study. Sensors. 2024;24:2115. doi: 10.3390/s24072115.

Chacón R., Posada H., Ramonell C., Sierra P., Rodríguez A., Koulalis I., Ioannidis K., Vrochidis S., Tomar R., Freitag S., et al. Bridge Safety, Maintenance, Management, Life-Cycle, Resilience and Sustainability, Proceedings of the Eleventh International Conference on Bridge Maintenance, Safety and Management (IABMAS 2022), Barcelona, Spain, 11–15 July 2022. CRC Press; Boca Raton, FL, USA: 2023. On the Digital Twinning of Load Tests in Railway Bridges. Case Study: High Speed Railway Network, Extremadura, Spain; pp. 819–827.

Naraniecki H., Lazoglu A., Marx S., Zaidman I. Concept for a Digital Twin of Railway Bridges on the Example of the New Filstal Bridges. Ce/Papers. 2023;6:711–717. doi: 10.1002/cepa.2050.

Padovano A., Longo F., Manca L., Grugni R. Improving Safety Management in Railway Stations through a Simulation-Based Digital Twin Approach. Comput. Ind. Eng. 2024;187:109839. doi: 10.1016/j.cie.2023.109839.

Ibrahim M., Rjabtšikov V., Gilbert R. Overview of Digital Twin Platforms for EV Applications. Sensors. 2023;23:1414. doi: 10.3390/s23031414.

Zhang Z., Zou Y., Zhou T., Zhang X., Xu Z. Energy Consumption Prediction of Electric Vehicles Based on Digital Twin Technology. World Electr. Veh. J. 2021;12:160. doi: 10.3390/wevj12040160.

Eaty N.D.K.M., Bagade P. Digital Twin for Electric Vehicle Battery Management with Incremental Learning. Expert Syst. Appl. 2023;229:120444. doi: 10.1016/j.eswa.2023.120444.

Karnehm D., Samanta A., Neve A., Williamson S. Five-Layer IoT and Fog Computing Framework Towards Digital Twinning of Battery Management Systems for e-Transportation; Proceedings of the 4th International Conference on Smart Grid and Renewable Energy, SGRE 2024—Proceedings; Doha, Qatar. 8–10 January 2024; Piscataway, NJ, USA: IEEE; 2024. pp. 1–7.

Zhang T., Liu X., Luo Z., Dong F., Jiang Y. Time Series Behavior Modeling with Digital Twin for Internet of Vehicles. Eurasip J. Wirel. Commun. Netw. 2019;271:1–12. doi: 10.1186/s13638-019-1589-8.

Jafari S., Byun Y.C. Prediction of the Battery State Using the Digital Twin Framework Based on the Battery Management System. IEEE Access. 2022;10:124685–124696. doi: 10.1109/ACCESS.2022.3225093.

Merkle L., Pöthig M., Schmid F. Estimate E-Golf Battery State Using Diagnostic Data and a Digital Twin. Batteries. 2021;7:15. doi: 10.3390/batteries7010015.

Li H., Bin Kaleem M., Chiu I.J., Gao D., Peng J., Huang Z. An Intelligent Digital Twin Model for the Battery Management Systems of Electric Vehicles. Int. J. Green Energy. 2023;21:461–475. doi: 10.1080/15435075.2023.2199330.

Li H., Bin Kaleem M., Chiu I.J., Gao D., Peng J. A Digital Twin Model for the Battery Management Systems of Electric Vehicles; Proceedings of the 2021 IEEE 23rd International Conference on High Performance Computing and Communications, 7th International Conference on Data Science and Systems, 19th International Conference on Smart City and 7th International Conference on Dependability in Sensor, Cloud & Big Data Systems & Applications; Haikou, China. 20–22 December 2021; Piscataway, NJ, USA: IEEE; 2022. pp. 1100–1107.

Venkatesan S., Manickavasagam K., Tengenkai N., Vijayalakshmi N. Health Monitoring and Prognosis of Electric Vehicle Motor Using Intelligent-Digital Twin. IET Electr. Power Appl. 2019;13:1328–1335. doi: 10.1049/iet-epa.2018.5732.

Kurukuru V.S.B., Khan M.A., Singh R. Health Monitoring Framework for Electric Vehicle Drive Train in Digital Twin; Proceedings of the 2023 25th European Conference on Power Electronics and Applications, EPE 2023 ECCE Europe; Aalborg, Denmark. 4–8 September 2023; Brussels, Belgium: EPE Association; 2023. pp. 1–10.

Suhaib Kamran S., Haleem A., Bahl S., Javaid M., Nandan D., Singh Verma A. Role of Smart Materials and Digital Twin (DT) for the Adoption of Electric Vehicles in India. Mater. Today Proc. 2021;52:2295–2304. doi: 10.1016/j.matpr.2021.09.249.

Elbakry M.S., Mahmoud A.M., Hassan S.E., Ismail T. Digital Twin Simulations for Connected and Automated Vehicles: A Comprehensive Study; Proceedings of the ICEEM 2023—3rd IEEE International Conference on Electronic Engineering; Menouf, Egypt. 7–8 October 2023; Piscataway, NJ, USA: IEEE; 2023. pp. 1–6.

Gürses A., Reddy G., Masrur S., Özdemir Ö., Güvenç İ., Sichitiu M.L., Şahin A., Alkhateeb A., Dutta R. Digital Twins for Supporting AI Research with Autonomous Vehicle Networks. IEEE Commun. Mag. 2024:1–7.

Schwarz C., Wang Z. The Role of Digital Twins in Connected and Automated Vehicles. IEEE Intell. Transp. Syst. Mag. 2022;14:41–51. doi: 10.1109/MITS.2021.3129524.

Heithoff M., Konersmann M., Michael J., Rumpe B., Steinfurth F. Challenges of Integrating Model-Based Digital Twins for Vehicle Diagnosis; Proceedings of the Proceedings—2023 ACM/IEEE International Conference on Model Driven Engineering Languages and Systems Companion, MODELS-C 2023; Västerås, Sweden. 1–6 October 2023; Piscataway, NJ, USA: IEEE; 2023. pp. 470–478.

Campolo C., Genovese G., Molinaro A., Pizzimenti B., Ruggeri G., Zappala D.M. An Edge-Based Digital Twin Framework for Connected and Autonomous Vehicles: Design and Evaluation. IEEE Access. 2024;12:46290–46303. doi: 10.1109/ACCESS.2024.3382001.

Rassolkin A., Vaimann T., Kallaste A., Kuts V. Digital Twin for Propulsion Drive of Autonomous Electric Vehicle; Proceedings of the 2019 IEEE 60th Annual International Scientific Conference on Power and Electrical Engineering of Riga Technical University, RTUCON 2019; Riga, Latvia. 7–9 October 2019; pp. 1–4.

Lei T., Sellers T., Luo C., Cao L., Bi Z. Digital Twin-based Multi-objective Autonomous Vehicle Navigation Approach as Applied in Infrastructure Construction. IET Cyber-Syst. Robot. 2024;6:e12110. doi: 10.1049/csy2.12110.

Wang X., Huang Z., Zheng S., Yu R., Pan M. Unpredictability of Digital Twin for Connected Vehicles. China Commun. 2023;20:26–45. doi: 10.23919/JCC.2023.02.003.

Ezhilarasu C.M., Skaf Z., Jennions I.K. Understanding the Role of a Digital Twin in Integrated Vehicle Health Management (IVHM); Proceedings of the 2019 IEEE International Conference on Systems, Man and Cybernetics (SMC); Bari, Italy. 6–9 October 2019; Piscataway, NJ, USA: IEEE; 2019. pp. 1484–1491.

Moloudi M.A., Foshati A., Kalantari H., Ejlali A. A Combination of FMEA and Digital Twinning for Rapid, Accurate, and Online Diagnosis in Vehicles Using COTS Embedded Computing Devices; Proceedings of the Proceedings—2022 CPSSI 4th International Symposium on Real-Time and Embedded Systems and Technologies, RTEST 2022; Tehran, Iran. 30–31 May 2022; Piscataway, NJ, USA: IEEE; 2022.

Bondarenko O., Fukuda T. Development of a Diesel Engine’s Digital Twin for Predicting Propulsion System Dynamics. Energy. 2020;196:117126. doi: 10.1016/j.energy.2020.117126.

Bo Y., Wu H., Che W., Zhang Z., Li X., Myagkov L. Methodology and Application of Digital Twin-Driven Diesel Engine Fault Diagnosis and Virtual Fault Model Acquisition. Eng. Appl. Artif. Intell. 2024;131:107853. doi: 10.1016/j.engappai.2024.107853.

Rajesh P.K., Manikandan N., Ramshankar C.S., Vishwanathan T., Sathishkumar C. Digital Twin of an Automotive Brake Pad for Predictive Maintenance. Procedia Comput. Sci. 2019;165:18–24. doi: 10.1016/j.procs.2020.01.061.

Venturini S., Rosso C., Velardocchia M. An Automotive Steel Wheel Digital Twin for Failure Identification under Accelerated Fatigue Tests. Eng. Fail. Anal. 2024;158:107979. doi: 10.1016/j.engfailanal.2024.107979.

Tomanik E., Jimenez-Reyes A.J., Tomanik V., Tormos B. Machine-Learning-Based Digital Twins for Transient Vehicle Cycles and Their Potential for Predicting Fuel Consumption. Vehicles. 2023;5:583–604. doi: 10.3390/vehicles5020032.

Pan Y.H., Wu N.Q., Qu T., Li P.Z., Zhang K., Guo H.F. Digital-Twin-Driven Production Logistics Synchronization System for Vehicle Routing Problems with Pick-up and Delivery in Industrial Park. Int. J. Comput. Integr. Manuf. 2021;34:814–828. doi: 10.1080/0951192X.2020.1829059.

Liu Q., Qi X., Liu S., Cheng X., Ke X., Wang F. Application of Lightweight Digital Twin System in Intelligent Transportation. IEEE J. Radio Freq. Identif. 2022;6:729–732. doi: 10.1109/JRFID.2022.3212169.

Kaytaz U., Ahmadian S., Sivrikaya F., Albayrak S. Graph Neural Network for Digital Twin-Enabled Intelligent Transportation System Reliability; Proceedings of the 2023 IEEE International Conference on Omni-Layer Intelligent Systems, COINS 2023; Berlin, Germany. 23–25 July 2023; Piscataway, NJ, USA: IEEE; 2023. pp. 1–7.

Wang Z., Gupta R., Han K., Wang H., Ganlath A., Ammar N., Tiwari P. Mobility Digital Twin: Concept, Architecture, Case Study, and Future Challenges. IEEE Internet Things J. 2022;9:17452–17467. doi: 10.1109/JIOT.2022.3156028.

Duan J., Wang Z., Jing X. Digital Twin Test Method with LTE-V2X for Autonomous Vehicle Safety Test. IEEE Internet Things J. 2024;vol. 11:1–11. doi: 10.1109/JIOT.2024.3435082.

Dorofeev A., Kurganov V., Filippova N., Petrov A., Zakharov D., Iarkov S. Improving Transportation Management Systems (TMSs) Based on the Concept of Digital Twins of an Organization. Appl. Sci. 2024;14:1330. doi: 10.3390/app14041330.

Cisneros Lombera D., Soualmi B., Sentouh C., Popieul J.C. Driver Model Using Fuzzy Logic for Virtual Validation. Adv. Transdiscipl. Eng. 2024;50:31–43. doi: 10.3233/ATDE240019.

Hasan Shuvo M.N., Zhu Q., Hossain M. Empowering Digital Twin: Early Action Decision through GAN-Enhanced Predictive Frame Synthesis for Autonomous Vehicles; Proceedings of the Proceedings—2023 IEEE/ACM Symposium on Edge Computing, SEC 2023; Wilmington, DE, USA. 6–9 December 2023; New York, NY, USA: ACM; 2023. pp. 330–335.

Ertürk M.A. Time Series Prediction with Digital Twins in Public Transportation Systems. Alphanumeric J. 2023;11:183–192. doi: 10.17093/alphanumeric.1402897.

Agavanakis K., Cassia J., Drombry M., Elkaim E. AIP Conference Proceedings. Volume 2437. AIP Publishing; Melville, NY, USA: 2022. Telemetry Transformation Towards Industry 4.0 Convergence—A Fuel Management Solution for the Transportation Sector Based on Digital Twins; pp. 1–23.

Zaidan R.A., Alamoodi A.H., Zaidan B.B., Zaidan A.A., Albahri O.S., Talal M., Garfan S., Sulaiman S., Mohammed A., Kareem Z.H., et al. Comprehensive Driver Behaviour Review: Taxonomy, Issues and Challenges, Motivations and Research Direction towards Achieving a Smart Transportation Environment. Eng. Appl. Artif. Intell. 2022;111:104745. doi: 10.1016/j.engappai.2022.104745.

Behboudi N., Moosavi S., Ramnath R. Recent Advances in Traffic Accident Analysis and Prediction: A Comprehensive Review of Machine Learning Techniques. arXiv. 20232406.13968v1

Abideen A.Z., Sundram V.P.K., Pyeman J., Othman A.K., Sorooshian S. Digital Twin Integrated Reinforced Learning in Supply Chain and Logistics. Logistics. 2021;5:84. doi: 10.3390/logistics5040084.

Marmolejo-Saucedo J.A. Design and Development of Digital Twins: A Case Study in Supply Chains. Mob. Networks Appl. 2020;25:2141–2160. doi: 10.1007/s11036-020-01557-9.

Park K.T., Son Y.H., Noh S. Do The Architectural Framework of a Cyber Physical Logistics System for Digital-Twin-Based Supply Chain Control. Int. J. Prod. Res. 2020;59:5721–5742. doi: 10.1080/00207543.2020.1788738.

Busse A., Gerlach B., Lengeling J.C., Poschmann P., Werner J., Zarnitz S. Towards Digital Twins of Multimodal Supply Chains. Logistics. 2021;5:25. doi: 10.3390/logistics5020025.

Yevu S.K., Owusu E.K., Chan A.P.C., Sepasgozar S.M.E., Kamat V.R. Digital Twin-Enabled Prefabrication Supply Chain for Smart Construction and Carbon Emissions Evaluation in Building Projects. J. Build. Eng. 2023;78:107598. doi: 10.1016/j.jobe.2023.107598.

Ashraf M., Eltawil A., Ali I. Disruption Detection for a Cognitive Digital Supply Chain Twin Using Hybrid Deep Learning. Volume 24. Springer; Berlin/Heidelberg, Germany: 2024.

Lee D., Lee S. Digital Twin for Supply Chain Coordination in Modular Construction. Appl. Sci. 2021;11:5909. doi: 10.3390/app11135909.

Ivanov D., Dolgui A. A Digital Supply Chain Twin for Managing the Disruption Risks and Resilience in the Era of Industry 4.0. Prod. Plan. Control. 2021;32:775–788. doi: 10.1080/09537287.2020.1768450.

Wu W., Shen L., Zhao Z., Harish A.R., Zhong R.Y., Huang G.Q. Internet of Everything and Digital Twin Enabled Service Platform for Cold Chain Logistics. J. Ind. Inf. Integr. 2023;33:100443. doi: 10.1016/j.jii.2023.100443.

Xu L., Proselkov Y., Schoepf S., Minarsch D., Minaricova M., Brintrup A. Implementation of Autonomous Supply Chains for Digital Twinning: A Multi-Agent Approach. IFAC-PapersOnLine. 2023;56:11076–11081. doi: 10.1016/j.ifacol.2023.10.812.

Zhang L., Wang X., Lin H., Piran M.J. A Crowdsourcing Logistics Solution Based on Digital Twin and Four-Party Evolutionary Game. Eng. Appl. Artif. Intell. 2024;130:107797. doi: 10.1016/j.engappai.2023.107797.

Coraddu A., Oneto L., Ilardi D., Stoumpos S., Theotokatos G. Marine Dual Fuel Engines Monitoring in the Wild through Weakly Supervised Data Analytics. Eng. Appl. Artif. Intell. 2021;100:104179. doi: 10.1016/j.engappai.2021.104179.

Stoumpos S., Theotokatos G. A Novel Methodology for Marine Dual Fuel Engines Sensors Diagnostics and Health Management. Int. J. Engine Res. 2022;23:974–994. doi: 10.1177/1468087421998635.

Tsitsilonis K.M., Theotokatos G., Patil C., Coraddu A. Health Assessment Framework of Marine Engines Enabled by Digital Twins. Int. J. Engine Res. 2023;24:3264–3281. doi: 10.1177/14680874221146835.

VanDerHorn E., Wang Z., Mahadevan S. Towards a Digital Twin Approach for Vessel-Specific Fatigue Damage Monitoring and Prognosis. Reliab. Eng. Syst. Saf. 2022;219:108222. doi: 10.1016/j.ress.2021.108222.

Bhagavathi R., Kwame Minde Kufoalor D., Hasan A. Digital Twin-Driven Fault Diagnosis for Autonomous Surface Vehicles. IEEE Access. 2023;11:41096–41104. doi: 10.1109/ACCESS.2023.3268711.

Hasan A., Asfihani T., Osen O., Bye R.T. Leveraging Digital Twins for Fault Diagnosis in Autonomous Ships. Ocean Eng. 2024;292:116546. doi: 10.1016/j.oceaneng.2023.116546.

Bickford J., Van Bossuyt D.L., Beery P., Pollman A. Operationalizing Digital Twins through Model-Based Systems Engineering Methods. Syst. Eng. 2020;23:724–750. doi: 10.1002/sys.21559.

Yao H., Wang D., Su M., Qi Y. Application of Digital Twins in Port System. J. Phys. Conf. Ser. 2021;1846:1–7. doi: 10.1088/1742-6596/1846/1/012008.

Wang K., Hu Q., Zhou M., Zun Z., Qian X. Multi-Aspect Applications and Development Challenges of Digital Twin-Driven Management in Global Smart Ports. Case Stud. Transp. Policy. 2021;9:1298–1312. doi: 10.1016/j.cstp.2021.06.014.

Zhou C., Xu J., Miller-Hooks E., Zhou W., Chen C.H., Lee L.H., Chew E.P., Li H. Analytics with Digital-Twinning: A Decision Support System for Maintaining a Resilient Port. Decis. Support Syst. 2021;143:113496. doi: 10.1016/j.dss.2021.113496.

Aghamohammadghaem M., Azucena J., Liao H., Zhang S., Nachtmann H. A Digital Twin for Visualizing, Evaluating and Maintaining Multimodal Transportation August 2021–September 2023. [(accessed on 1 July 2024)];2023 Available online:

Li Y., Chang D., Gao Y., Zou Y., Bao C. Automated Container Terminal Production Operation and Optimization via an AdaBoost-Based Digital Twin Framework. J. Adv. Transp. 2021;2021:1–16. doi: 10.1155/2021/1936764.

Szpytko J., Salgado Duarte Y. A Digital Twins Concept Model for Integrated Maintenance: A Case Study for Crane Operation. J. Intell. Manuf. 2021;32:1863–1881. doi: 10.1007/s10845-020-01689-5.

Zhou Y., Fu Z., Zhang J., Li W., Gao C. A Digital Twin-Based Operation Status Monitoring System for Port Cranes. Sensors. 2022;22:3216. doi: 10.3390/s22093216.

Gao Y., Chang D., Chen C.H., Xu Z. Design of Digital Twin Applications in Automated Storage Yard Scheduling. Adv. Eng. Inform. 2022;51:101477. doi: 10.1016/j.aei.2021.101477.

Kutzke D.T., Carter J.B., Hartman B.T. Subsystem Selection for Digital Twin Development: A Case Study on an Unmanned Underwater Vehicle. Ocean Eng. 2021;223:108629. doi: 10.1016/j.oceaneng.2021.108629.

Berti N., Serena F. Digital Twin and Human Factors in Manufacturing and Logistics Systems: State of the Art and Future Research Directions. IFAC-PapersOnLine. 2022;55:1893–1898. doi: 10.1016/j.ifacol.2022.09.675.

Schislyaeva E.R., Kovalenko E.A. Innovations in Logistics Networks on the Basis of the Digital Twin. Acad. Strateg. Manag. J. 2021;20:1–17.

Kivrak H., Baniqued P.D.E., Watson S., Lennox B. An Investigation of the Network Characteristics and Requirements of 3D Environmental Digital Twins for Inspection Robots; Proceedings of the 2022 IEEE 23rd International Symposium on a World of Wireless, Mobile and Multimedia Networks, WoWMoM; Belfast, UK. 14–17 June 2022; Piscataway, NJ, USA: IEEE; 2022. pp. 596–600.

Williams R., Erkoyuncu J.A., Masood T., Vrabic R. Augmented Reality Assisted Calibration of Digital Twins of Mobile Robots. IFAC-PapersOnLine. 2020;53:203–208. doi: 10.1016/j.ifacol.2020.11.033.

Ellethy M., George M., Abouzeid A., Shaaban A., Elgammal A., Adham R., Abdelsalam M., Elbatt T. A Digital Twin Architecture for Automated Guided Vehicles Using a Dockerized Private Cloud; Proceedings of the 2023 IEEE Smart World Congress (SWC); Portsmouth, UK. 28–31 August 2023; pp. 1–8.

Bozhdaraj D., Lucke D., Jooste J.L. Smart Maintenance Architecture for Automated Guided Vehicles. Procedia CIRP. 2023;118:110–115. doi: 10.1016/j.procir.2023.06.020.

Zong X., Luan Y., Wang H., Li S. A Multi-Robot Monitoring System Based on Digital Twin. Procedia Comput. Sci. 2021;183:94–99. doi: 10.1016/j.procs.2021.02.035.

Liu X., Jiang D., Tao B., Jiang G., Sun Y., Kong J., Tong X., Zhao G., Chen B. Genetic Algorithm-Based Trajectory Optimization for Digital Twin Robots. Front. Bioeng. Biotechnol. 2022;9:1–11. doi: 10.3389/fbioe.2021.793782.

Azangoo M., Taherkordi A., Blech J.O., Vyatkin V. Digital Twin-Assisted Controlling of AGVs in Flexible Manufacturing Environments; Proceedings of the IEEE International Symposium on Industrial Electronics; Kyoto, Japan. 20–23 June 2021; Piscataway, NJ, USA: IEEE; 2021. pp. 1–7.

Al-Samahi S.S., Al-Darraji I.A. Digital Twin-Based Decision-Making Technique for Diagnostic 2D Environment Line Following Error of Mobile Robot; Proceedings of the 21st International Multi-Conference on Systems, Signals & Devices (SSD); Erbil, Iraq. 22–25 April 2024; Piscataway, NJ, USA: IEEE Xplore; 2024. pp. 278–285.

Gyulai D., Bergmann J., Lengyel A., Kadar B., Czirkó D. Simulation-Based Digital Twin of a Complex Shop-Floor Logistic System; Proceedings of the 2020 Winter Simulation Conference; Orlando, FL, USA. 14–18 December 2020; pp. 1849–1860.

Lichtenstern I., Kerber F. Data-Based Digital Twin of an Automated Guided Vehicle System; Proceedings of the 2022 Winter Simulation Conference; Singapore. 11–14 December 2022; Piscataway, NJ, USA: IEEE; 2022. pp. 2936–2946.

Stączek P., Pizoń J., Danilczuk W., Gola A. A Digital Twin Approach for the Improvement of an Autonomous Mobile Robots (AMR’s) Operating Environment—A Case Study. Sensors. 2021;21:7830. doi: 10.3390/s21237830.

Li J., Liu M., Wang W., Hu C. Inspection Robot Based on Offline Digital Twin Synchronization Architecture. IEEE J. Radio Freq. Identif. 2022;6:943–947. doi: 10.1109/JRFID.2022.3207047.

Majdzik P., Witczak M., Lipiec B., Banaszak Z. Integrated Fault-Tolerant Control of Assembly and Automated Guided Vehicle-Based Transportation Layers. Int. J. Comput. Integr. Manuf. 2022;35:409–426. doi: 10.1080/0951192X.2021.1872103.

Bhatti G., Singh R.R. Intelligent Fault Diagnosis Mechanism for Industrial Robot Actuators Using Digital Twin Technology; Proceedings of the 2021 IEEE International Power and Renewable Energy Conference, IPRECON 2021; Kollam, India. 24–26 September 2021; Piscataway, NJ, USA: IEEE; 2021. pp. 1–6.

Szpytko J., Duarte Y.S. Integrated Maintenance Platform for Critical Cranes under Operation: Database for Maintenance Purposes. IFAC-PapersOnLine. 2020;53:167–172. doi: 10.1016/j.ifacol.2020.11.027.

Hu X., Assaad R.H. A BIM-Enabled Digital Twin Framework for Real-Time Indoor Environment Monitoring and Visualization by Integrating Autonomous Robotics, LiDAR-Based 3D Mobile Mapping, IoT Sensing, and Indoor Positioning Technologies. J. Build. Eng. 2024;86:108901. doi: 10.1016/j.jobe.2024.108901.

Lou P., Zhong Y., Hu J., Fan C., Chen X. Digital-Twin-Driven AGV Scheduling and Routing in Automated Container Terminals. Mathematics. 2023;11:2678. doi: 10.3390/math11122678.

Gao Y., Chang D., Chen C.H., Sha M. A Digital Twin-Based Decision Support Approach for AGV Scheduling. Eng. Appl. Artif. Intell. 2024;130:107687. doi: 10.1016/j.engappai.2023.107687.

Zhang L., Wan H., Zheng X., Tian M., Liu Y., Su L. Digital-Twin Prediction of Metamorphic Object Transportation by Multi-Robots with THz Communication Framework. IEEE Trans. Intell. Transp. Syst. 2022;24:7757–7765. doi: 10.1109/TITS.2022.3229657.

Coelho F., Relvas S., Barbosa-Póvoa A.P. Simulation-Based Decision Support Tool for in-House Logistics: The Basis for a Digital Twin. Comput. Ind. Eng. 2021;153:107094. doi: 10.1016/j.cie.2020.107094.

Rauscher F., Fischer G., Lehmann T., Zapata J.J., Pagani P., Loving A. A Digital Twin Concept for the Development of a DEMO Maintenance Logistics Modelling Tool. Fusion Eng. Des. 2021;168:112399. doi: 10.1016/j.fusengdes.2021.112399.

Grigoriev S.N., Dolgov V.A., Nikishechkin P.A., Dolgov N.V. Information Model of Production and Logistics Systems of Machine-Building Enterprises as the Basis for the Development and Maintenance of Their Digital Twins. IOP Conf. Ser. Mater. Sci. Eng. 2020;971:032094. doi: 10.1088/1757-899X/971/3/032094.

Pires F., Ahmad B., Moreira A.P., Leitão P. Recommendation System Using Reinforcement Learning for What-If Simulation in Digital Twin; Proceedings of the IEEE International Conference on Industrial Informatics (INDIN); Palma de Mallorca, Spain. 21–23 July 2021.

Maheshwari P., Kamble S., Kumar S., Belhadi A., Gupta S. Digital Twin-Based Warehouse Management System: A Theoretical Toolbox for Future Research and Applications. Int. J. Logist. Manag. 2023;35:1073–1106. doi: 10.1108/IJLM-01-2023-0030.

Hauge J.B., Zafarzadeh M., Jeong Y., Li Y., Khilji W.A., Wiktorsson M. Employing Digital Twins within Production Logistics; Proceedings of the Proceedings—2020 IEEE International Conference on Engineering, Technology and Innovation, ICE/ITMC 2020; Cardiff, UK. 15–17 June 2020; pp. 1–8.

Wang Y., Jiang Z., Wu Y. Model Construction of Material Distribution System Based on Digital Twin. Int. J. Adv. Manuf. Technol. 2022;121:4485–4501. doi: 10.1007/s00170-022-09636-9.

Miao J., Lan S. Application of Visual Sensing Image Processing Technology under Digital Twins to the Intelligent Logistics System. Adv. Civ. Eng. 2021;2021:1–13. doi: 10.1155/2021/5743387.

Guo M., Fang X., Wu Q., Zhang S., Li Q. Joint Multi-Objective Dynamic Scheduling of Machine Tools and Vehicles in a Workshop Based on Digital Twin. J. Manuf. Syst. 2023;70:345–358. doi: 10.1016/j.jmsy.2023.07.011.

Hu B., Guo H., Tao X., Zhang Y. Construction of Digital Twin System for Cold Chain Logistics Stereo Warehouse. IEEE Access. 2023;11:73850–73862. doi: 10.1109/ACCESS.2023.3295819.

Fath A., Hanna N., Liu Y., Tanch S., Xia T., Huston D. Indoor Infrastructure Maintenance Framework Using Networked Sensors, Robots, and Augmented Reality Human Interface. Futur. Internet. 2024;16:170. doi: 10.3390/fi16050170.

Fedorko G., Molnar V., Stehlikova B., Michalik P., Saliga J. Design of Evaluation Classification Algorithm for Identifying Conveyor Belt Mistracking in a Continuous Transport System’s Digital Twin. Sensors. 2024;24:3810. doi: 10.3390/s24123810.

He F., Ong S.K., Nee A.Y.C. An Integrated Mobile Augmented Reality Digital Twin Monitoring System. Computers. 2021;10:99. doi: 10.3390/computers10080099.

Zhao Z., Shen L., Yang C., Wu W., Zhang M., Huang G.Q. IoT and Digital Twin Enabled Smart Tracking for Safety Management. Comput. Oper. Res. 2021;128:105183. doi: 10.1016/j.cor.2020.105183.

Lopes T.D., Raizer A., Júnior W.V. The Use of Digital Twins in Finite Element for the Study of Induction Motors Faults. Sensors. 2021;21:7833. doi: 10.3390/s21237833.

Santos J.F.D., Tshoombe B.K., Santos L.H.B., Araujo R.C.F., Manito A.R.A., Fonseca W.S., Silva M.O. Digital Twin-Based Monitoring System of Induction Motors Using IoT Sensors and Thermo-Magnetic Finite Element Analysis. IEEE Access. 2023;11:1682–1693. doi: 10.1109/ACCESS.2022.3232063.

Rjabtsikov V., Ibrahim M., Asad B., Rassolkin A., Vaimann T., Kallaste A., Kuts V., Stepien M., Krawczyk M. Digital Twin Service Unit Development for an EV Induction Motor Fault Detection; Proceedings of the 2023 IEEE International Electric Machines and Drives Conference, IEMDC 2023; San Francisco, CA, USA. 15–18 May 2023; Piscataway, NJ, USA: IEEE; 2023. pp. 1–5.

Yue M., Benaggoune K., Meng J., Diallo D. Implementation of an Early Stage Fuel Cell Degradation Prediction Digital Twin Based on Transfer Learning. IEEE Trans. Transp. Electrif. 2023;9:3308–3318. doi: 10.1109/TTE.2022.3229716.

Yang D., Cui Y., Xia Q., Jiang F., Ren Y., Sun B., Feng Q., Wang Z., Yang C. A Digital Twin-Driven Life Prediction Method of Lithium-Ion Batteries Based on Adaptive Model Evolution. Materials. 2022;15:3331. doi: 10.3390/ma15093331.

Xie X., Yang Z., Wu W., Zhang L., Wang X., Zeng G., Chen G. Fault Diagnosis Method for Bearing Based on Digital Twin. Math. Probl. Eng. 2022;2022:1–15. doi: 10.1155/2022/2982746.

Piltan F., Toma R.N., Shon D., Im K., Choi H.K., Yoo D.S., Kim J.M. Strict-Feedback Backstepping Digital Twin and Machine Learning Solution in AE Signals for Bearing Crack Identification. Sensors. 2022;22:539. doi: 10.3390/s22020539.

Li Z., Ruan D., Wang J., Yan J., Gühmann C. Bearing Digital Twin Based on Response Model and Reinforcement Learning. Lubricants. 2023;11:502. doi: 10.3390/lubricants11120502.

Feng K., Ji J.C., Zhang Y., Ni Q., Liu Z., Beer M. Digital Twin-Driven Intelligent Assessment of Gear Surface Degradation. Mech. Syst. Signal Process. 2023;186:1–23. doi: 10.1016/j.ymssp.2022.109896.

Gao P., Zhao S., Zheng Y. Failure Prediction of Coal Mine Equipment Braking System Based on Digital Twin Models. Processes. 2024;12:837. doi: 10.3390/pr12040837.

Zhang W., Liu Z., Liao Z. Digital Twin Inspired Intelligent Bearing Fault Diagnosis Method Based on Adaptive Correlation Filtering and Improved SAE Classification Model. Math. Probl. Eng. 2022;2022:1–17. doi: 10.1155/2022/8767974.

Zhao X., Wang W., Wen L., Chen Z., Wu S., Zhou K., Sun M., Xu L., Hu B., Wu C. Digital Twins in Smart Farming: An Autoware-Based Simulator for Autonomous Agricultural Vehicles. Int. J. Agric. Biol. Eng. 2023;16:184–189. doi: 10.25165/j.ijabe.20231604.8039.

Matania O., Bechhoefer E., Bortman J. Digital Twin of a Gear Root Crack Prognosis. Sensors. 2023;23:9883. doi: 10.3390/s23249883.

Chen Q., Zhu Z., Si S., Cai Z. Intelligent Maintenance of Complex Equipment Based on Blockchain and Digital Twin Technologies; Proceedings of the IEEE International Conference on Industrial Engineering and Engineering Management; Singapore. 14–17 December 2020; pp. 908–912.

Automation Systems and Integration—Digital Twin Framework for Manufacturing—Part 1: Overview and General Principles. ISO; Geneva, Switzerland: 2020.

Automation Systems and Integration—Digital Twin Framework for Manufacturing—Part 2: Reference Architecture. ISO; Geneva, Switzerland: 2021.

Automation Systems and Integration—Digital Twin Framework for Manufacturing—Part 3: Digital Representation of Manufacturing Elements. ISO; Geneva, Switzerland: 2020.

Automation Systems and Integration—Digital Twin Framework for Manufacturing—Part 4: Information Exchange. ISO; Geneva, Switzerland: 2021.

This section collects any data citations, data availability statements, or supplementary materials included in this article.