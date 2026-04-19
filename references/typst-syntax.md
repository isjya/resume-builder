# Syntax

Typst is a markup language. This means that you can use simple syntax to accomplish common layout tasks. The lightweight markup syntax is complemented by set and show rules, which let you style your document easily and automatically. All this is backed by a tightly integrated scripting language with built-in and user-defined functions.

## Modes

Typst has three syntactical modes: Markup, math, and code. Markup mode is the default in a Typst document, math mode lets you write mathematical formulas, and code mode lets you use Typst's scripting features.

You can switch to a specific mode at any point by referring to the following table:

| New mode | Syntax                        | Example                       |
| -------- | ----------------------------- | ----------------------------- |
| Code     | Prefix the code with `#`      | `Number: #(1 + 2)`            |
| Math     | Surround equation with `$..$` | `$-x$ is the opposite of $x$` |
| Markup   | Surround markup with `[..]`   | `let name = [*Typst!*]`       |

Once you have entered code mode with `#`, you don't need to use further hashes unless you switched back to markup or math mode in between.

## Markup

Typst provides built-in markup for the most common document elements. Most of the syntax elements are just shortcuts for a corresponding function. The table below lists all markup that is available and links to the best place to learn more about their syntax and usage.

| Name             | Example                  | See                                                          |
| ---------------- | ------------------------ | ------------------------------------------------------------ |
| Paragraph break  | Blank line               | [`parbreak`](https://typst.app/docs/reference/model/parbreak/) |
| Strong emphasis  | `*strong*`               | [`strong`](https://typst.app/docs/reference/model/strong/)   |
| Emphasis         | `_emphasis_`             | [`emph`](https://typst.app/docs/reference/model/emph/)       |
| Raw text         | ``print(1)``             | [`raw`](https://typst.app/docs/reference/text/raw/)          |
| Link             | `https://typst.app/`     | [`link`](https://typst.app/docs/reference/model/link/)       |
| Label            | `<intro>`                | [`label`](https://typst.app/docs/reference/foundations/label/) |
| Reference        | `@intro`                 | [`ref`](https://typst.app/docs/reference/model/ref/)         |
| Heading          | `= Heading`              | [`heading`](https://typst.app/docs/reference/model/heading/) |
| Bullet list      | `- item`                 | [`list`](https://typst.app/docs/reference/model/list/)       |
| Numbered list    | `+ item`                 | [`enum`](https://typst.app/docs/reference/model/enum/)       |
| Term list        | `/ Term: description`    | [`terms`](https://typst.app/docs/reference/model/terms/)     |
| Math             | `$x^2$`                  | [Math](https://typst.app/docs/reference/math/)               |
| Line break       | `\`                      | [`linebreak`](https://typst.app/docs/reference/text/linebreak/) |
| Smart quote      | `'single' or "double"`   | [`smartquote`](https://typst.app/docs/reference/text/smartquote/) |
| Symbol shorthand | `~`, `---`               | [Symbols](https://typst.app/docs/reference/symbols/sym/)     |
| Code expression  | `#rect(width: 1cm)`      | [Scripting](https://typst.app/docs/reference/scripting/#expressions) |
| Character escape | `Tweet at us \#ad`       | [Below](https://typst.app/docs/reference/syntax/#escapes)    |
| Comment          | `/* block */`, `// line` | [Below](https://typst.app/docs/reference/syntax/#comments)   |

## Math mode

Math mode is a special markup mode that is used to typeset mathematical formulas. It is entered by wrapping an equation in `$` characters. This works both in markup and code. The equation will be typeset into its own block if it starts and ends with at least one space (e.g. `$ x^2 $`). Inline math can be produced by omitting the whitespace (e.g. `$x^2$`). An overview over the syntax specific to math mode follows:

| Name                   | Example               | See                                                          |
| ---------------------- | --------------------- | ------------------------------------------------------------ |
| Inline math            | `$x^2$`               | [Math](https://typst.app/docs/reference/math/)               |
| Block-level math       | `$ x^2 $`             | [Math](https://typst.app/docs/reference/math/)               |
| Bottom attachment      | `$x_1$`               | [`attach`](https://typst.app/docs/reference/math/attach/)    |
| Top attachment         | `$x^2$`               | [`attach`](https://typst.app/docs/reference/math/attach/)    |
| Fraction               | `$1 + (a+b)/5$`       | [`frac`](https://typst.app/docs/reference/math/frac/)        |
| Line break             | `$x \ y$`             | [`linebreak`](https://typst.app/docs/reference/text/linebreak/) |
| Alignment point        | `$x &= 2 \ &= 3$`     | [Math](https://typst.app/docs/reference/math/)               |
| Variable access        | `$#x$, $pi$`          | [Math](https://typst.app/docs/reference/math/)               |
| Field access           | `$arrow.r.long$`      | [Scripting](https://typst.app/docs/reference/scripting/#fields) |
| Implied multiplication | `$x y$`               | [Math](https://typst.app/docs/reference/math/)               |
| Symbol shorthand       | `$->$`, `$!=$`        | [Symbols](https://typst.app/docs/reference/symbols/sym/)     |
| Text/string in math    | `$a "is natural"$`    | [Math](https://typst.app/docs/reference/math/)               |
| Math function call     | `$floor(x)$`          | [Math](https://typst.app/docs/reference/math/)               |
| Code expression        | `$#rect(width: 1cm)$` | [Scripting](https://typst.app/docs/reference/scripting/#expressions) |
| Character escape       | `$x\^2$`              | [Below](https://typst.app/docs/reference/syntax/#escapes)    |
| Comment                | `$/* comment */$`     | [Below](https://typst.app/docs/reference/syntax/#comments)   |

## Code mode

Within code blocks and expressions, new expressions can start without a leading `#` character. Many syntactic elements are specific to expressions. Below is a table listing all syntax that is available in code mode:

| Name                     | Example                       | See                                                          |
| ------------------------ | ----------------------------- | ------------------------------------------------------------ |
| None                     | `none`                        | [`none`](https://typst.app/docs/reference/foundations/none/) |
| Auto                     | `auto`                        | [`auto`](https://typst.app/docs/reference/foundations/auto/) |
| Boolean                  | `false`, `true`               | [`bool`](https://typst.app/docs/reference/foundations/bool/) |
| Integer                  | `10`, `0xff`                  | [`int`](https://typst.app/docs/reference/foundations/int/)   |
| Floating-point number    | `3.14`, `1e5`                 | [`float`](https://typst.app/docs/reference/foundations/float/) |
| Length                   | `2pt`, `3mm`, `1em`, ..       | [`length`](https://typst.app/docs/reference/layout/length/)  |
| Angle                    | `90deg`, `1rad`               | [`angle`](https://typst.app/docs/reference/layout/angle/)    |
| Fraction                 | `2fr`                         | [`fraction`](https://typst.app/docs/reference/layout/fraction/) |
| Ratio                    | `50%`                         | [`ratio`](https://typst.app/docs/reference/layout/ratio/)    |
| String                   | `"hello"`                     | [`str`](https://typst.app/docs/reference/foundations/str/)   |
| Label                    | `<intro>`                     | [`label`](https://typst.app/docs/reference/foundations/label/) |
| Math                     | `$x^2$`                       | [Math](https://typst.app/docs/reference/math/)               |
| Raw text                 | ``print(1)``                  | [`raw`](https://typst.app/docs/reference/text/raw/)          |
| Variable access          | `x`                           | [Scripting](https://typst.app/docs/reference/scripting/#blocks) |
| Code block               | `{ let x = 1; x + 2 }`        | [Scripting](https://typst.app/docs/reference/scripting/#blocks) |
| Content block            | `[*Hello*]`                   | [Scripting](https://typst.app/docs/reference/scripting/#blocks) |
| Parenthesized expression | `(1 + 2)`                     | [Scripting](https://typst.app/docs/reference/scripting/#blocks) |
| Array                    | `(1, 2, 3)`                   | [Array](https://typst.app/docs/reference/foundations/array/) |
| Dictionary               | `(a: "hi", b: 2)`             | [Dictionary](https://typst.app/docs/reference/foundations/dictionary/) |
| Unary operator           | `-x`                          | [Scripting](https://typst.app/docs/reference/scripting/#operators) |
| Binary operator          | `x + y`                       | [Scripting](https://typst.app/docs/reference/scripting/#operators) |
| Assignment               | `x = 1`                       | [Scripting](https://typst.app/docs/reference/scripting/#operators) |
| Field access             | `x.y`                         | [Scripting](https://typst.app/docs/reference/scripting/#fields) |
| Method call              | `x.flatten()`                 | [Scripting](https://typst.app/docs/reference/scripting/#methods) |
| Function call            | `min(x, y)`                   | [Function](https://typst.app/docs/reference/foundations/function/) |
| Argument spreading       | `min(..nums)`                 | [Arguments](https://typst.app/docs/reference/foundations/arguments/) |
| Unnamed function         | `(x, y) => x + y`             | [Function](https://typst.app/docs/reference/foundations/function/) |
| Let binding              | `let x = 1`                   | [Scripting](https://typst.app/docs/reference/scripting/#bindings) |
| Named function           | `let f(x) = 2 * x`            | [Function](https://typst.app/docs/reference/foundations/function/) |
| Set rule                 | `set text(14pt)`              | [Styling](https://typst.app/docs/reference/styling/#set-rules) |
| Set-if rule              | `set text(..) if ..`          | [Styling](https://typst.app/docs/reference/styling/#set-rules) |
| Show-set rule            | `show heading: set block(..)` | [Styling](https://typst.app/docs/reference/styling/#show-rules) |
| Show rule with function  | `show raw: it => {..}`        | [Styling](https://typst.app/docs/reference/styling/#show-rules) |
| Show-everything rule     | `show: template`              | [Styling](https://typst.app/docs/reference/styling/#show-rules) |
| Context expression       | `context text.lang`           | [Context](https://typst.app/docs/reference/context/)         |
| Conditional              | `if x == 1 {..} else {..}`    | [Scripting](https://typst.app/docs/reference/scripting/#conditionals) |
| For loop                 | `for x in (1, 2, 3) {..}`     | [Scripting](https://typst.app/docs/reference/scripting/#loops) |
| While loop               | `while x < 10 {..}`           | [Scripting](https://typst.app/docs/reference/scripting/#loops) |
| Loop control flow        | `break, continue`             | [Scripting](https://typst.app/docs/reference/scripting/#loops) |
| Return from function     | `return x`                    | [Function](https://typst.app/docs/reference/foundations/function/) |
| Include module           | `include "bar.typ"`           | [Scripting](https://typst.app/docs/reference/scripting/#modules) |
| Import module            | `import "bar.typ"`            | [Scripting](https://typst.app/docs/reference/scripting/#modules) |
| Import items from module | `import "bar.typ": a, b, c`   | [Scripting](https://typst.app/docs/reference/scripting/#modules) |
| Comment                  | `/* block */`, `// line`      | [Below](https://typst.app/docs/reference/syntax/#comments)   |

## Comments

Comments are ignored by Typst and will not be included in the output. This is useful to exclude old versions or to add annotations. To comment out a single line, start it with `//`:

```
// our data barely supports
// this claim

We show with $p < 0.05$
that the difference is
significant.
```

Comments can also be wrapped between `/*` and `*/`. In this case, the comment can span over multiple lines:

```
Our study design is as follows:
/* Somebody write this up:
   - 1000 participants.
   - 2x2 data design. */
```

## Escape sequences

Escape sequences are used to insert special characters that are hard to type or otherwise have special meaning in Typst. To escape a character, precede it with a backslash. To insert any Unicode codepoint, you can write a hexadecimal escape sequence: `\u{1f600}`. The same kind of escape sequences also work in [strings](https://typst.app/docs/reference/foundations/str/).

```
I got an ice cream for
\$1.50! \u{1f600}
```

### Typst Escape Characters Quick Guide

Backslash `\` cancels the syntax meaning of special characters in **markup mode** (only basic escapes work in code/strings).

## Core Escapes

- `\#`: Escapes function/code prefix

  ```
  \#1
  ```

   not 

  ```
  #1
  ```

- `\+`: Escapes ordered list prefix (line-start only)

  ```
  \+ Not a list
  ```

- `\-`: Escapes unordered list prefix (line-start only)

  ```
  \- Not a list
  ```

- `\@`: Escapes label/citation prefix

  ```
  user\@gmail.com
  ```

- `\*`/`\_`: Escapes bold/italic markers

  ```
  \*asterisk\*
  ```

- `\``: Escapes inline code marker

  ```
  \`backtick\`
  ```

- `\$`: Escapes math formula marker

  ```
  \$1.50
  ```

- `\[`/`\]`/`\(`/`\)`: Escapes link/footnote markers

  ```
  \[bracket\]
  ```

- `\{`/`\}`: Escapes grouping/brace markers

  ```
  \{brace\}
  ```

- `\\`: Escapes backslash itself

  ```
  \\
  ```

## Key Rules

- Only escape syntax characters in **markup mode**
- Inline special characters (e.g., `1+1`) never need escaping
- Strings only require escaping: `\\`/`\"`/`\n`/`\r`/`\t`/`\u{XXXX}`
- Code blocks/math blocks need no escaping (except their own delimiters)

## Identifiers

Names of variables, functions, and so on (*identifiers*) can contain letters, numbers, hyphens (`-`), and underscores (`_`). They must start with a letter or an underscore.

More specifically, the identifier syntax in Typst is based on the [Unicode Standard Annex #31](https://www.unicode.org/reports/tr31/), with two extensions: Allowing `_` as a starting character, and allowing both `_` and `-` as continuing characters.

For multi-word identifiers, the recommended case convention is [Kebab case](https://en.wikipedia.org/wiki/Letter_case#Kebab_case). In Kebab case, words are written in lowercase and separated by hyphens (as in `top-edge`). This is especially relevant when developing modules and packages for others to use, as it keeps things predictable.

```
#let kebab-case = [Using hyphen]
#let _schön = "😊"
#let 始料不及 = "😱"
#let π = calc.pi

#kebab-case
#if -π < 0 { _schön } else { 始料不及 }
// -π means -1 * π,
// so it's not a valid identifier
```

## Paths

Typst has various features that require a file path to reference external resources such as images, Typst files, or data files. Paths are represented as [strings](https://typst.app/docs/reference/foundations/str/). There are two kinds of paths: Relative and absolute.

- A **relative path** searches from the location of the Typst file where the feature is invoked. It is the default:

  ```
  #image("images/logo.png")
  ```

- An **absolute path** searches from the *root* of the project. It starts with a leading `/`:

  ```
  #image("/assets/logo.png")
  ```

### Project root

By default, the project root is the parent directory of the main Typst file. For security reasons, you cannot read any files outside of the root directory.

If you want to set a specific folder as the root of your project, you can use the CLI's `--root` flag. Make sure that the main file is contained in the folder's subtree!

```
typst compile --root .. file.typ
```

In the web app, the project itself is the root directory. You can always read all files within it, no matter which one is previewed (via the eye toggle next to each Typst file in the file panel).

### Paths and packages

A package can only load files from its own directory. Within it, absolute paths point to the package root, rather than the project root. For this reason, it cannot directly load files from the project directory. If a package needs resources from the project (such as a logo image), you must pass the already loaded image, e.g. as a named parameter `logo: image("mylogo.svg")`. Note that you can then still customize the image's appearance with a set rule within the package.

In the future, paths might become a [distinct type from strings](https://github.com/typst/typst/issues/971), so that they can retain knowledge of where they were constructed. This way, resources could be loaded from a different root.
