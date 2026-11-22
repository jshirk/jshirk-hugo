---
title: "{{ replace (replaceRE `^\d{4}-\d{2}-\d{2}-` "" .File.ContentBaseName) "-" " " | title }}"
author: "Jordan Shirkman"
date: {{ .Date }}   # original publish date; never change it later
slug: /{{ replaceRE `^\d{4}-\d{2}-\d{2}-` "" .File.ContentBaseName }}/
categories:
  - Methodology   # one of: Theology, Technology, Methodology
description: ""
draft: true
# Dates are not shown to readers. To show "Last updated" after a meaningful
# revision, uncomment both lines and set lastmod to the revision date:
# lastmod: YYYY-MM-DDT00:00:00+00:00
# showLastUpdated: true
---
