-- kidscode-breaks.lua: let long code names wrap instead of running into the margin.
--
-- File paths and identifiers such as grade-4-6/1-introductory/exercises/week07/... or
-- ModuleNotFoundError, set in the monospace font inside running text or narrow
-- table cells, contain no spaces, so TeX cannot break them and they stick out of
-- the margin (worst in the larger dyslexia-friendly edition).
--
-- Before each paragraph is broken into lines, this adds an optional break point
-- (a penalty node, no hyphen is shown):
--   * after "/" and "_"                      (cheap)
--   * after "." and "-"                      (a little dearer)
--   * between a lower-case and an upper-case letter, as in NotFound (dearer still)
-- but only between two glyphs of a monospace font, so prose is untouched.
-- A break is only taken when a line would otherwise overflow.

local GLYPH = node.id("glyph")
local mono_cache = {}

local function is_mono(fid)
  local v = mono_cache[fid]
  if v == nil then
    local fd = font.getfont(fid)
    local name = fd and (fd.name or fd.fullname or fd.psname) or ""
    v = name:find("Mono") ~= nil
    mono_cache[fid] = v
  end
  return v
end

local AFTER = { [47] = 50, [95] = 50, [46] = 400, [45] = 200 } -- / _ . -
local CAMEL = 300

local function is_lower(c) return c >= 97 and c <= 122 end
local function is_upper(c) return c >= 65 and c <= 90 end

local function add_breaks(head)
  local n = head
  while n do
    local nxt = n.next
    if n.id == GLYPH and nxt and nxt.id == GLYPH and is_mono(n.font) and is_mono(nxt.font) then
      local p = AFTER[n.char]
      if not p and is_lower(n.char) and is_upper(nxt.char) then
        p = CAMEL
      end
      if p then
        local pen = node.new("penalty")
        pen.penalty = p
        head = node.insert_after(head, n, pen)
      end
    end
    n = nxt
  end
  return head
end

luatexbase.add_to_callback("pre_linebreak_filter", function(head)
  return add_breaks(head)
end, "kidscode.codebreaks")
