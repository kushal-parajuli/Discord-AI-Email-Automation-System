# Discord AI Email Automation System

## Project Overview

Discord AI Email Automation System is an AI-powered workflow automation project that enables users to generate and send professional emails directly from Discord.

The system integrates Discord, Python, n8n, Ollama AI, Docker, and SMTP email services to automate the complete email creation and delivery process.

Users simply provide a command in Discord, and the system automatically:

* Extracts the recipient email address
* Extracts the email topic
* Generates a professional email using AI
* Creates an appropriate subject line
* Sends the email to the specified recipient

---

## Project Status

✅ Completed and Fully Functional

### Implemented Features

* Discord Bot Integration
* n8n Workflow Automation
* Ollama AI Integration
* Professional Email Generation
* SMTP Email Delivery
* Dynamic Recipient Selection
* Automated Subject Generation
* Local AI Processing

---

## Problem Statement

Writing professional emails repeatedly can be time-consuming and inefficient.

This project demonstrates how Artificial Intelligence and workflow automation can be combined to automatically generate and send professional emails using simple Discord commands.

---

## Objectives

* Automate email generation using AI
* Send emails directly from Discord commands
* Learn workflow automation using n8n
* Integrate multiple technologies into a single solution
* Demonstrate practical AI automation concepts
* Explore real-world business automation workflows

---

## System Architecture

```text
**Discord User
      ↓
Discord Bot (Python)
      ↓
n8n Webhook
      ↓
Edit Fields Node
      ↓
Ollama AI Model (Llama 3.2)
      ↓
Code Node (Subject & Body Extraction)
      ↓
SMTP Email Service
      ↓
Recipient Inbox**
```

---

## Technologies Used

### Programming Language

* Python 

### Python Libraries

* discord.py
* requests

### Workflow Automation

* n8n
* Docker

### Artificial Intelligence

* Ollama
* Llama 3.2

### Communication Platform

* Discord

### Email Service

* Gmail SMTP

### Version Control

* Git
* GitHub

---

## Features

### AI Email Generation

Automatically generates professional emails based on a user-provided topic.

### Discord Integration

Accepts commands directly from Discord.

### Automated Email Delivery

Sends generated emails automatically using SMTP.

### Dynamic Recipient Selection

Allows users to specify any valid recipient email address.

### Local AI Processing

Uses Ollama locally without relying on external cloud-based AI services.

### Workflow Automation

Automates the complete process from user request to email delivery.

---

## Demo

### Input

```text
sendmail recipient@gmail.com Internship Application
```

### Processing

1. Discord Bot receives the command
2. Python extracts recipient and topic
3. Data is sent to n8n through a webhook
4. Ollama generates a professional email
5. Subject and body are processed
6. SMTP sends the email

### Output

```text
Subject: Application for Summer Internship Position

Dear Hiring Manager,

I am writing to express my interest in the summer internship position...

Best regards,

Kushal Parajuli
```

---

## Command Format

```text
sendmail recipient@example.com Email Topic
```

### Examples

```text
sendmail john@gmail.com Internship Application
```

```text
sendmail manager@gmail.com Project Deadline Reminder
```

```text
sendmail recruiter@gmail.com Software Developer Job Application
```

---

## Workflow Explanation

### Step 1: Discord Message

The user sends a command in Discord.

Example:

```text
sendmail john@gmail.com Internship Application
```

### Step 2: Python Discord Bot

The bot:

* Reads the message
* Extracts recipient information
* Extracts topic information
* Sends data to n8n

### Step 3: n8n Webhook

Receives structured data:

```json
{
  "recipient": "john@gmail.com",
  "topic": "Internship Application"
}
```

### Step 4: AI Email Generation

Ollama generates:

* Subject Line
* Professional Email Body

### Step 5: Subject and Body Processing

The Code Node separates:

* Email Subject
* Email Body

### Step 6: Email Delivery

SMTP sends the generated email to the specified recipient.

---

## Installation Guide

### Clone Repository

```bash
https://github.com/kushal-parajuli/Discord-AI-Email-Automation-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama:

https://ollama.com

Pull the required model:

```bash
ollama pull llama3.2
```

### Start n8n

```bash
docker start n8n
```

### Run Discord Bot

```bash
python bot.py
```

### Open n8n

```text
http://localhost:5678
```

---

## Required Configuration

### Discord Bot Token

Replace:

```python
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
```

with your own Discord Bot Token.

### SMTP Credentials

Configure Gmail SMTP credentials inside the n8n Email node.

### Ollama Model

Ensure Ollama is running locally and Llama 3.2 is installed.

---

## Project Structure

```text
Discord_Email_Bot/
│
├── bot.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

---

## Sample Email Output

```text
Subject: Project Deadline Reminder

Dear Team,

This is a friendly reminder that our current project is nearing its deadline. Please review your progress and ensure all assigned tasks are completed on schedule.

Thank you for your cooperation.

Best regards,

Kushal Parajuli
```

---

## Real-World Applications

This project demonstrates automation concepts used by businesses for:

* Customer Support Automation
* Email Marketing
* Lead Management
* CRM Integration
* Help Desk Automation
* Social Media Automation
* AI-Powered Communication Systems

---


## Learning Outcomes

This project demonstrates:

* Workflow Automation
* AI Integration
* Discord Bot Development
* SMTP Email Automation
* Docker Usage
* Webhook Communication
* API Integration
* Local LLM Deployment
* GitHub Project Management

---
### Kushal Parajuli
GitHub: https://github.com/kushal-parajuli
