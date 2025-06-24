---
title: "🎨 Font Styling Guide"
date: "2025-06-21"
tags: ["guide", "styling", "css"]
---

This post demonstrates different ways to style text in your markdown files.

## 1. Method 1: Using Headings

You can use Markdown headings for consistent styling:

### 1.1. Colors
- Use **normal text** for default color.
- Use `h4` for highlight: 

#### Highlighted text

- Use `h5` for quote:

##### Quoted text

- Use `h6` for inline code style:

###### Inline code style

### 1.2. Font Sizes
- `#` Main Heading (post title)
- `##` Heading
- `###` Subheading
- Normal text for body

### 1.3. Font Weights
- Use `**bold**` for bold text
- Use `*italic*` for italic text

### 1.4. Text Alignment
- Alignment is not directly supported in Markdown, but you can use lists and indentation for structure.

## 2. Method 2: Inline HTML (Advanced)

For more specific styling, you can use inline HTML, but it's recommended to use Markdown headings for best compatibility.

## 3. Tips for Best Practices

1. **Use Markdown headings** for consistent styling across your blog
2. **Use inline HTML** only for one-off custom styling
3. **Keep colors consistent** with your blog's theme
4. **Don't overuse** - too much styling can be distracting
5. **Test readability** - ensure text remains legible

## 4. Available CSS Classes

### 4.1. Colors
- `text-red`, `text-teal`, `text-blue`, `text-green`, `text-purple`, `text-orange`

### 4.2. Sizes
- `text-small`, `text-medium`, `text-large`, `text-xl`, `text-xxl`

### 4.3. Weights
- `text-light`, `text-normal`, `text-bold`, `text-extra-bold`

### 4.4. Alignment
 `text-center`, `text-right`, `text-left`

### 4.5. Special
- `highlight`, `quote`, `code-inline`