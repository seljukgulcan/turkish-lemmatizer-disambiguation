#!/home/seljuk/miniconda3/envs/python2/bin/python

from __future__ import print_function
import sys
from trnltk.morphology.contextless.parser.test.parser_test import ParserTest
from trnltk.morphology.lexicon.lexiconloader import LexiconLoader
from trnltk.morphology.lexicon.rootgenerator import CircumflexConvertingRootGenerator, RootMapGenerator
from trnltk.morphology.model import formatter
from trnltk.morphology.morphotactics.basicsuffixgraph import BasicSuffixGraph
from trnltk.morphology.morphotactics.copulasuffixgraph import CopulaSuffixGraph
from trnltk.morphology.contextless.parser.parser import  logger as parser_logger, UpperCaseSupportingContextlessMorphologicalParser
from trnltk.morphology.contextless.parser.rootfinder import WordRootFinder, DigitNumeralRootFinder, TextNumeralRootFinder, ProperNounFromApostropheRootFinder, ProperNounWithoutApostropheRootFinder
from trnltk.morphology.contextless.parser.suffixapplier import logger as suffix_applier_logger
from trnltk.morphology.morphotactics.numeralsuffixgraph import NumeralSuffixGraph
from trnltk.morphology.morphotactics.predefinedpaths import PredefinedPaths

from trnltk.morphology.morphotactics.propernounsuffixgraph import ProperNounSuffixGraph

all_roots = []

lexemes = LexiconLoader.load_from_file('trnltk/trnltk/resources/master_dictionary.txt')
for di in lexemes:
	all_roots.extend(CircumflexConvertingRootGenerator.generate(di))

root_map_generator = RootMapGenerator()
root_map = root_map_generator.generate(all_roots)

suffix_graph = CopulaSuffixGraph(NumeralSuffixGraph(ProperNounSuffixGraph(BasicSuffixGraph())))
suffix_graph.initialize()

predefined_paths = PredefinedPaths(root_map, suffix_graph)
predefined_paths.create_predefined_paths()

word_root_finder = WordRootFinder(root_map)
text_numeral_root_finder = TextNumeralRootFinder(root_map)
digit_numeral_root_finder = DigitNumeralRootFinder()
proper_noun_from_apostrophe_root_finder = ProperNounFromApostropheRootFinder()
proper_noun_without_apostrophe_root_finder = ProperNounWithoutApostropheRootFinder()

parser = UpperCaseSupportingContextlessMorphologicalParser(suffix_graph, predefined_paths,
	[word_root_finder, text_numeral_root_finder, digit_numeral_root_finder,
	 proper_noun_from_apostrophe_root_finder, proper_noun_without_apostrophe_root_finder])

sentence = sys.argv[1].decode('utf-8')

for word in sentence.split():
	lst = parser.parse(word)
	root_set = set()
	for element in lst:
		formatted = formatter.format_morpheme_container_for_parseset(element)
		root = formatted[:formatted.index('+')]
		root_set.add(root.lower())

	for root in root_set:
		print(root.encode('utf-8'), end=' ')
	print()