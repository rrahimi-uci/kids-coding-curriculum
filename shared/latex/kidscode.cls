%% kidscode.cls -- shared document class for the Kids Coding curriculum
%%
%% Engine: LuaLaTeX (fontspec). Build with `make pdf` from the repo root.
%%
%% Class options
%%   level=1|2|3      level number (sets accent color + running header)
%%   track=main|junior  main track (Grades 4-5, default) or junior track
%%                    (Grades 2-3: 14pt type, junior level names; see
%%                    docs/JUNIOR-SYLLABUS.md)
%%   teacher          marks the document TEACHER ONLY (banner + header)
%%   student          (default) student-facing document
%%
%% Variant: define \kcvariant before loading the class to switch fonts.
%%   lualatex "\def\kcvariant{dyslexia}\input{file.tex}"
%%   -> Lexend Deca, larger size, 1.5 line spacing, extra letter/word
%%      spacing, cream page, no italics, ragged-right text.
%%
%% All colors come from the Okabe-Ito color-blind-safe palette and every
%% colored box also carries a text label + symbol, so meaning never
%% depends on color alone. See docs/AUTHORING.md for the macro reference.

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{kidscode}[2026/11/07 Kids Coding curriculum class]

\RequirePackage{kvoptions}
\SetupKeyvalOptions{family=kc,prefix=kc@}
\DeclareStringOption[1]{level}
\DeclareStringOption[main]{track}
\DeclareBoolOption{teacher}
\DeclareComplementaryOption{student}{teacher}
\ProcessKeyvalOptions*

\newif\ifkc@dyslexia
\ifdefined\kcvariant
  \def\kc@dysname{dyslexia}
  \ifx\kcvariant\kc@dysname \kc@dyslexiatrue \fi
\fi

\newif\ifkc@junior
\def\kc@juniorname{junior}
\ifx\kc@track\kc@juniorname \kc@juniortrue \fi

\ifkc@junior
  %% Junior pages are read aloud by a grown-up and followed by 7-9-year-olds:
  %% 14pt type in both editions (the dyslexia edition adds its own spacing).
  \LoadClass[14pt]{extarticle}
\else\ifkc@dyslexia
  \LoadClass[12pt]{article}
\else
  \LoadClass[11pt]{article}
\fi\fi

%% ---------------------------------------------------------------- packages
\RequirePackage{iftex}
\ifLuaTeX\else
  \ClassError{kidscode}{Please compile with LuaLaTeX}{Run: make pdf}
\fi
\RequirePackage{fontspec}
\RequirePackage[letterpaper,margin=0.8in,headheight=15pt,includehead,includefoot]{geometry}
\RequirePackage[table]{xcolor}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,shapes.misc,calc,fit,backgrounds,decorations.pathreplacing}
\RequirePackage[most]{tcolorbox}
\RequirePackage{enumitem}
\RequirePackage{array,booktabs,tabularx,longtable,multicol,makecell}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{titlesec}
\RequirePackage{etoolbox}
\RequirePackage{setspace}
\RequirePackage{ragged2e}
\RequirePackage{amssymb}
\RequirePackage{pifont}
\RequirePackage{listings}
\RequirePackage{needspace}
\RequirePackage{fontawesome5}
\RequirePackage{scratch3}
\setdefaultscratch{else word=else}
\RequirePackage{microtype}
\RequirePackage{newunicodechar}
\RequirePackage[autostyle]{csquotes}
\RequirePackage[hidelinks,bookmarksnumbered]{hyperref}

%% ---------------------------------------------------------------- fonts
\ifkc@dyslexia
  \setmainfont{LexendDeca-Regular.ttf}[
    Ligatures = TeX,
    BoldFont = LexendDeca-Regular.ttf,
    BoldFeatures = {FakeBold=2.2},
    ItalicFont = LexendDeca-Regular.ttf,
    BoldItalicFont = LexendDeca-Regular.ttf,
    BoldItalicFeatures = {FakeBold=2.2},
    LetterSpace = 3.0,
    WordSpace = {1.4,1.2,1.0}]
  \setsansfont{LexendDeca-Regular.ttf}[
    Ligatures = TeX,
    BoldFont = LexendDeca-Regular.ttf,
    BoldFeatures = {FakeBold=2.2},
    LetterSpace = 3.0]
  \renewcommand{\emph}[1]{\textbf{#1}}
  \setstretch{1.5}
  \AtBeginDocument{\RaggedRight}
  \pagecolor[HTML]{FDF8E7}
\else
  \setmainfont{AtkinsonHyperlegibleNext}[
    Extension = .otf, Ligatures = TeX,
    UprightFont = *-Regular,
    BoldFont = *-Bold,
    ItalicFont = *-RegularItalic,
    BoldItalicFont = *-BoldItalic]
  \setsansfont{AtkinsonHyperlegibleNext}[
    Extension = .otf, Ligatures = TeX,
    UprightFont = *-Regular,
    BoldFont = *-Bold,
    ItalicFont = *-RegularItalic,
    BoldItalicFont = *-BoldItalic]
  \setstretch{1.15}
\fi
\setmonofont{AtkinsonHyperlegibleMono}[
  Extension = .otf,
  UprightFont = *-Regular,
  BoldFont = *-Bold,
  ItalicFont = *-RegularItalic,
  BoldItalicFont = *-BoldItalic,
  Scale = MatchLowercase]

\renewcommand{\textrightarrow}{\ensuremath{\rightarrow}}
\newunicodechar{✓}{\checkmark}
\newunicodechar{✗}{\ding{55}}
\newunicodechar{★}{\faStar}
\newunicodechar{→}{\ensuremath{\rightarrow}}
\newunicodechar{←}{\ensuremath{\leftarrow}}
\newunicodechar{↑}{\ensuremath{\uparrow}}
\newunicodechar{↓}{\ensuremath{\downarrow}}
\newunicodechar{×}{\ensuremath{\times}}
\newunicodechar{÷}{\ensuremath{\div}}
\newunicodechar{≠}{\ensuremath{\neq}}
\newunicodechar{≤}{\ensuremath{\leq}}
\newunicodechar{≥}{\ensuremath{\geq}}

%% Long code names and paths may wrap after / _ . - (see kidscode-breaks.lua).
\directlua{dofile(kpse.find_file("kidscode-breaks.lua", "tex"))}

\setlength{\emergencystretch}{3em}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}

%% ---------------------------------------------------------------- colors
%% Okabe-Ito palette (color-blind safe), shared with the parent slide deck.
\RequirePackage{kidscode-colors}

\ifcase\kc@level\relax
  \colorlet{kcaccent}{kcblue}\or
  \colorlet{kcaccent}{kcblue}\or
  \colorlet{kcaccent}{kcgreen}\or
  \colorlet{kcaccent}{kcvermillion}\else
  \colorlet{kcaccent}{kcblue}
\fi

\ifkc@junior
  \newcommand{\kclevelname}{%
    \ifcase\kc@level\relax\or Level 1: Little Robots\or Level 2: Game Makers\or Level 3: Bridge to Python\fi}
  \newcommand{\kctrackname}{Kids Coding Junior}
\else
  \newcommand{\kclevelname}{%
    \ifcase\kc@level\relax\or Level 1: Introduction\or Level 2: Intermediate\or Level 3: Advanced\fi}
  \newcommand{\kctrackname}{Kids Coding}
\fi
\newcommand{\kclevelnumber}{\kc@level}

%% ---------------------------------------------------------------- headings
\titleformat{\section}{\needspace{6\baselineskip}\Large\bfseries\color{kcaccent}}{\thesection}{0.6em}{}
\titleformat{\subsection}{\large\bfseries}{\thesubsection}{0.6em}{}
\titleformat{\subsubsection}{\normalsize\bfseries}{\thesubsubsection}{0.6em}{}
\setcounter{secnumdepth}{0}
\setcounter{tocdepth}{2}
%% Week banners are level-0 TOC entries; weekly documents set tocdepth to 0
%% so their contents list shows one line per week (\kcweeklytoc).
\newcommand*{\l@kcweek}{\@dottedtocline{0}{0pt}{2.6em}}
\newcommand{\kcweeklytoc}{\setcounter{tocdepth}{0}\tableofcontents}

%% ---------------------------------------------------------------- header/footer
\newcommand{\kc@doctitle}{}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\fancyhead[L]{\small\textbf{\kctrackname} \textperiodcentered{} \kclevelname}
\fancyhead[R]{\small\kc@doctitle\ifkc@teacher\ \textperiodcentered\ \textbf{TEACHER ONLY}\fi}
\fancyfoot[C]{\small Page \thepage\ of \pageref*{LastPage}}
\fancypagestyle{plain}{\fancyhf{}\renewcommand{\headrulewidth}{0pt}%
  \fancyfoot[C]{\small Page \thepage\ of \pageref*{LastPage}}}

%% ---------------------------------------------------------------- cover page
%% \kctitle{Document title}{Short subtitle / audience line}
\newcommand{\kctitle}[2]{%
  \renewcommand{\kc@doctitle}{#1}%
  \hypersetup{pdftitle={\kctrackname\ - \kclevelname\ - #1}}%
  \thispagestyle{plain}%
  \begin{tikzpicture}[remember picture,overlay]
    \fill[kcaccent] (current page.north west) rectangle ([yshift=-1.2cm]current page.north east);
    \foreach \c [count=\i] in {kcorange,kcsky,kcgreen,kcyellow,kcblue,kcvermillion,kcpurple}
      \fill[\c] ([xshift={(\i-1)*3cm},yshift=-1.2cm]current page.north west) rectangle ++(3cm,-0.25cm);
  \end{tikzpicture}%
  \vspace*{2.2cm}
  {\color{kcgray}\Large\bfseries \kctrackname{} \textperiodcentered{} \kclevelname\par}
  \vspace{0.6cm}
  {\fontsize{30}{36}\selectfont\bfseries #1\par}
  \vspace{0.4cm}
  {\Large #2\par}
  \ifkc@teacher
    \vspace{0.6cm}
    \kcteacherbanner
  \fi
  \ifkc@dyslexia
    \vspace{0.4cm}{\small Dyslexia-friendly edition (Lexend, wider spacing).\par}
  \fi
  \vspace{0.8cm}
}

\newcommand{\kcteacherbanner}{%
  \begin{tcolorbox}[colback=kcvermillion!8,colframe=kcvermillion,boxrule=1.2pt,arc=2pt,left=6pt]
  \textbf{\faLock\ TEACHER ONLY.} Keep this document away from students: it contains answers,
  reference solutions or assessment keys.
  \end{tcolorbox}}

%% ---------------------------------------------------------------- code
\lstdefinestyle{kcpython}{
  language=Python,
  basicstyle=\ttfamily\small\setstretch{1.0},
  keywordstyle=\bfseries\color{kcblue},
  stringstyle=\color{kcvermillion!85!black},
  commentstyle=\itshape\color{kcgray},
  showstringspaces=false,
  columns=fullflexible,
  keepspaces=true,
  breaklines=true,
  breakatwhitespace=true,
  postbreak=\mbox{\textcolor{kcgray}{$\hookrightarrow$}\space},
  numbers=left,
  numberstyle=\tiny\color{kcgray},
  numbersep=6pt,
  tabsize=4,
  upquote=true,
  morekeywords={True,False,None,self},
  literate={✓}{{\checkmark}}1 {→}{{$\rightarrow$}}1 {×}{{$\times$}}1 {…}{{\ldots}}1 {—}{{---}}1 {–}{{--}}1 {é}{{\'e}}1
}
\lstdefinestyle{kcshell}{
  language={}, keywordstyle={}, stringstyle={}, commentstyle={},
  basicstyle=\ttfamily\small\setstretch{1.0},
  columns=fullflexible, keepspaces=true, breaklines=true, numbers=none,
  upquote=true, showstringspaces=false
}
\lstset{style=kcpython}

\tcbset{kccode/.style={enhanced,breakable,colback=kcsky!7,colframe=kcsky!70!black,
  boxrule=0.6pt,arc=2pt,left=14pt,right=4pt,top=2pt,bottom=2pt}}

%% Code blocks are framed boxes on their own. Inside another box (answer,
%% workedexample, ...) they become a left-ruled listing instead, because a
%% box inside a box cannot break across pages.
\newif\ifkc@inbox
\lstdefinestyle{kcinbox}{frame=leftline,framerule=1.6pt,rulecolor=\color{kcsky!70!black},
  xleftmargin=1.6em,framexleftmargin=1.4em,aboveskip=6pt,belowskip=6pt}
\newcommand{\kc@codeopen}[1]{\par\ifkc@inbox\else\begin{tcolorbox}[kccode,#1]\fi}
\newcommand{\kc@codeclose}{\ifkc@inbox\else\end{tcolorbox}\fi}

%% Python code block: \begin{pycode}[optional title] ... \end{pycode}
\lstnewenvironment{pycode}[1][]{%
  \lstset{style=kcpython}%
  \ifkc@inbox\lstset{style=kcinbox}\fi
  \ifstrempty{#1}{}{\lstset{title={\small\bfseries\color{kcblue}#1}}}%
}{}
\BeforeBeginEnvironment{pycode}{\kc@codeopen{}}
\AfterEndEnvironment{pycode}{\kc@codeclose}

%% Shell / Terminal block
\lstnewenvironment{shellcode}{\lstset{style=kcshell}\ifkc@inbox\lstset{style=kcinbox,rulecolor=\color{kcgray},title={\small\faTerminal\ Terminal}}\fi}{}
\BeforeBeginEnvironment{shellcode}{\kc@codeopen{colback=kcblack!4,colframe=kcgray,left=6pt,title={\small\faTerminal\ Terminal}}}
\AfterEndEnvironment{shellcode}{\kc@codeclose}

%% Program output block
\lstnewenvironment{outputcode}{\lstset{style=kcshell}\ifkc@inbox\lstset{style=kcinbox,rulecolor=\color{kcgray!60},title={\small Output}}\fi}{}
\BeforeBeginEnvironment{outputcode}{\kc@codeopen{colback=kcblack!3,colframe=kcgray!60,left=6pt,title={\small Output}}}
\AfterEndEnvironment{outputcode}{\kc@codeclose}

%% Include a tested code file: \pyfile{../exercises/week07/square/solution.py}
\newcommand{\pyfile}[2][]{\par
  \ifkc@inbox
    \lstinputlisting[style=kcpython,style=kcinbox,title={\small\faFile*[regular]\ \texttt{\detokenize{#2}}},#1]{#2}%
  \else
    \begin{tcolorbox}[kccode,title={\small\faFile*[regular]\ \texttt{\detokenize{#2}}}]%
    \lstinputlisting[style=kcpython,#1]{#2}\end{tcolorbox}%
  \fi}
%% Inline code: \py{print("hi")}  (use a delimiter-safe argument)
\newcommand{\py}{\lstinline[style=kcpython,basicstyle=\ttfamily\normalsize,columns=fullflexible]}

%% ---------------------------------------------------------------- boxes
%% Generic labeled box. Every box has an icon AND a word label.
\newtcolorbox{kc@box}[3][]{enhanced,breakable,colback=#2!8,colframe=#2!80!black,
  boxrule=0.8pt,arc=2pt,left=6pt,right=6pt,top=4pt,bottom=4pt,
  fonttitle=\bfseries,coltitle=black,colbacktitle=#2!35,
  title={#3},before upper={\kc@inboxtrue},#1}

\newenvironment{objectives}{\begin{kc@box}{kcblue}{\faBullseye\ Learning objectives}\begin{itemize}[leftmargin=1.2em,itemsep=2pt]}{\end{itemize}\end{kc@box}}
\newenvironment{materials}{\begin{kc@box}{kcgray}{\faToolbox\ Materials \& preparation}\begin{itemize}[leftmargin=1.2em,itemsep=1pt]}{\end{itemize}\end{kc@box}}
\newenvironment{teacherscript}[1][Say]{\begin{kc@box}[colback=white]{kcorange}{\faComment*[regular]\ Teacher script: #1}}{\end{kc@box}}
\newenvironment{analogy}[1][]{\begin{kc@box}{kcyellow}{\faLightbulb[regular]\ Kid-friendly analogy\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{unplugged}[1][]{\begin{kc@box}{kcgreen}{\faCut\ Unplugged activity (no computer)\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{bughunt}[1][]{\begin{kc@box}{kcvermillion}{\faBug\ Bug hunt\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{pairroles}[1][]{\begin{kc@box}{kcpurple}{\faUserFriends\ Pair programming\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{freebuild}[1][]{\begin{kc@box}{kcsky}{\faPaintBrush\ Creative free-build\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{reflection}[1][]{\begin{kc@box}{kcpurple}{\faPenFancy\ Reflection\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{formativecheck}[1][]{\begin{kc@box}{kcblue}{\faCheckCircle[regular]\ Formative check\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{commonmistakes}{\begin{kc@box}{kcvermillion}{\faExclamationTriangle\ Common mistakes}\begin{itemize}[leftmargin=1.2em,itemsep=2pt]}{\end{itemize}\end{kc@box}}
\newenvironment{differentiation}{\begin{kc@box}{kcgreen}{\faHandsHelping\ Differentiation}}{\end{kc@box}}
\newcommand{\supportpath}{\par\textbf{\faArrowDown\ Support path (needs more time):}\ }
\newcommand{\extensionpath}{\par\textbf{\faArrowUp\ Extension path (finished early):}\ }
\newenvironment{stretchchallenge}[1][]{\begin{kc@box}{kcorange}{\faRocket\ Stretch challenge\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{workedexample}[1][]{\begin{kc@box}[colback=white]{kcblue}{\faChalkboardTeacher\ Worked example\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{tip}[1][]{\begin{kc@box}{kcsky}{\faInfoCircle\ Tip\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{safety}[1][]{\begin{kc@box}{kcgreen}{\faShield*\ Digital citizenship \& safety\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{teachernote}[1][]{\begin{kc@box}{kcgray}{\faStickyNote[regular]\ Teacher note\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{scratchspec}[1][]{\begin{kc@box}[colback=white]{kcorange}{\faCat\ Scratch exercise\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}

%% Vocabulary box:  \begin{vocab} \vocabword{loop}{Code that repeats.} \end{vocab}
\newenvironment{vocab}{\begin{kc@box}{kcyellow}{\faBook\ Vocabulary box}\begin{description}[leftmargin=0pt,itemsep=2pt,font=\bfseries]}{\end{description}\end{kc@box}}
\newcommand{\vocabword}[2]{\item[#1] #2}

%% Numbered exercises (workbook, in class): \begin{exercise}[Title] ... \end{exercise}
\newcounter{kcexercise}
\newcommand{\kc@week}{0}
\newenvironment{exercise}[1][]{\stepcounter{kcexercise}%
  \begin{kc@box}{kcblue}{\faLaptopCode\ Exercise \kc@week.\arabic{kcexercise}\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}

%% Homework tiers
\newenvironment{core}[1][]{\begin{kc@box}{kcblue}{\faStar\ Core (everyone)\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{challenge}[1][]{\begin{kc@box}{kcorange}{\faStar\faStar\ Challenge (want more?)\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{creative}[1][]{\begin{kc@box}{kcpurple}{\faPalette\ Creative (make it yours)\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{selfcheck}{\begin{kc@box}{kcgreen}{\faClipboardCheck\ Self-check: check off each box when it is true}\begin{itemize}[label=$\square$,leftmargin=1.5em,itemsep=2pt]}{\end{itemize}\end{kc@box}}
\newenvironment{checklist}[1][Checklist]{\begin{itemize}[label=$\square$,leftmargin=1.5em,itemsep=2pt]}{\end{itemize}}

%% Answer key boxes
\newenvironment{answer}[1][]{\begin{kc@box}[colback=white]{kcgreen}{\faKey\ Answer\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
\newenvironment{rubric}[1][]{\begin{kc@box}{kcblue}{\faTable\ Rubric\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}

%% ---------------------------------------------------------------- junior track
%% Defined only for track=junior, so main-track documents that define their own
%% \ican or similar helpers are not affected.
\ifkc@junior
%% Student goals as "I can ..." statements (junior workbook chapters):
%%   \begin{ican} \item I can ... \end{ican}
\newenvironment{ican}{\begin{kc@box}{kcblue}{\faStar\ I can \ldots}\begin{itemize}[label={\faStar[regular]},leftmargin=1.6em,itemsep=2pt]}{\end{itemize}\end{kc@box}}
%% A short note for the grown-up who reads the page aloud.
\newenvironment{grownup}[1][]{\begin{kc@box}{kcgray}{\faUserFriends\ For the grown-up\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
%% Junior homework: one optional 5-10 minute card, done with a grown-up.
\newenvironment{playathome}[1][]{\begin{kc@box}{kcpurple}{\faHome\ Play at home (5--10 minutes, with a grown-up)\ifstrempty{#1}{}{: #1}}}{\end{kc@box}}
%% Show-me checklist (observed, never graded):
%%   \begin{showme}[Week 5] \showmerow{Puts arrow cards in order} \end{showme}
\newenvironment{showme}[1][]{\par\noindent\textbf{\faEye[regular]\ Show me\ifstrempty{#1}{}{: #1}}\par\nopagebreak\noindent
  \renewcommand{\arraystretch}{1.5}%
  \tabularx{\linewidth}{@{}X>{\centering\arraybackslash}p{1.9cm}>{\centering\arraybackslash}p{1.9cm}>{\centering\arraybackslash}p{1.9cm}@{}}
  \toprule \rowcolor{kcaccent!15} \textbf{The child can \ldots} & \small Not yet & \small Getting there & \small Got it\\ \midrule}
  {\bottomrule\endtabularx\par}
\newcommand{\showmerow}[1]{#1 & $\square$ & $\square$ & $\square$\\}
\fi

%% ---------------------------------------------------------------- lesson structure
%% \lesson{7}{Hello, Python!}{one-line big idea}
\newcommand{\lesson}[3]{%
  \clearpage
  \renewcommand{\kc@week}{#1}\setcounter{kcexercise}{0}%
  \phantomsection
  \addcontentsline{toc}{kcweek}{Week #1: #2}%
  \begin{tcolorbox}[enhanced,colback=kcaccent,colframe=kcaccent,coltext=white,arc=2pt,left=8pt]
    {\large\bfseries Week #1}\hfill{\small\kclevelname}\par
    {\LARGE\bfseries #2}\par\smallskip
    {\normalsize #3}
  \end{tcolorbox}}
%% Workbook chapter / homework set / answers section use the same banner:
\let\chapterweek\lesson
\let\homeworkweek\lesson
\let\answersweek\lesson
%% Non-week sections (buffer sessions, appendices):  \kcpart{B1}{Title}{big idea}
\newcommand{\kcpart}[3]{%
  \clearpage
  \renewcommand{\kc@week}{#1}\setcounter{kcexercise}{0}%
  \phantomsection
  \addcontentsline{toc}{kcweek}{#1: #2}%
  \begin{tcolorbox}[enhanced,colback=kcgray,colframe=kcgray,coltext=white,arc=2pt,left=8pt]
    {\large\bfseries #1}\hfill{\small\kclevelname}\par
    {\LARGE\bfseries #2}\par\smallskip
    {\normalsize #3}
  \end{tcolorbox}}

%% At-a-glance line under a lesson banner:
%% \lessoninfo{Concepts: loops, range}{Tools: Thonny}{Standards: 1B-AP-10}
\newcommand{\lessoninfo}[3]{\par\noindent{\small\textbf{#1}\quad\textperiodcentered\quad\textbf{#2}\quad\textperiodcentered\quad\textbf{#3}}\par}

%% Minute-by-minute plan
%% \begin{timeplan}
%%   \timeslot{0--8}{Warm-up}{What happens, what to say/do}
%% \end{timeplan}
\newenvironment{timeplan}{\par\noindent\renewcommand{\arraystretch}{1.3}%
  \tabularx{\linewidth}{@{}>{\bfseries}p{1.6cm}>{\bfseries}p{2.6cm}X@{}}
  \toprule \rowcolor{kcaccent!15} Minutes & Phase & What happens\\ \midrule}
  {\bottomrule\endtabularx\par}
\newcommand{\timeslot}[3]{#1 & #2 & #3\\}

%% ---------------------------------------------------------------- writing space
\newcommand{\answerlines}[1]{\par\begin{tikzpicture}
  \foreach \i in {1,...,#1}{\draw[kcgray!60] (0,-\i*0.9) -- (\linewidth,-\i*0.9);}
  \end{tikzpicture}\par}
\newcommand{\answerspace}[1]{\par\noindent\begin{tikzpicture}\draw[kcgray!60,rounded corners=2pt] (0,0) rectangle (\linewidth,-#1);\end{tikzpicture}\par}
\newcommand{\tickbox}{$\square$}
\newcommand{\namedateline}{\par\noindent Name (nickname is fine): \rule{6cm}{0.4pt}\hfill Date: \rule{3.5cm}{0.4pt}\par\medskip}

%% Coverage table marks (introduce / revisit / extend)
\newcommand{\cvI}{\textbf{I}}
\newcommand{\cvR}{R}
\newcommand{\cvE}{\textbf{E}\textsuperscript{+}}

%% Key/keyboard rendering: \keys{Ctrl}
\newcommand{\keys}[1]{\tikz[baseline=(k.base)]\node[draw,rounded corners=2pt,inner sep=2pt,font=\small\ttfamily](k){#1};}
\newcommand{\menu}[1]{\textsf{\textbf{#1}}}

%% Okabe-Ito swatch: \swatch{kcorange}
\newcommand{\swatch}[1]{\tikz[baseline=-0.6ex]\fill[#1,draw=black] (0,0) rectangle (0.8em,-0.8em);}

%% Input a part file; shows a visible placeholder if it does not exist yet.
\newcommand{\kcinput}[1]{\IfFileExists{#1.tex}{\input{#1}}{\clearpage\textbf{[Missing file: \detokenize{#1}.tex]}}}

\endinput
