---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides the concepts common to all market rates, indices and indicators; that is concepts descriptive
      of the numeric parameters themselves. These are modeled independently of the values they may take over time.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group, Inc.\n\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Indicators Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20140601/Indicators/Indicators.rdf version of this ontology was
      modified per the issue resolutions identified in the FIBO IND 1.0 FTF 1 report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20160801/Indicators/Indicators.rdf version of this ontology was
      modified per the FIBO 2.0 RFC, namely, to integrate concepts recently added to the FND domain including Rate, ExchangeRate,
      InterestRate and StructuredCollection and revise definitions of TermStructure and Volatility to better support concepts
      such as yield curves and analysis of market rates generally.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20180801/Indicators/Indicators.rdf version of this ontology was
      modified to integrate the composite date value and reflect migration of statistical measures to Analytics.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20190501/Indicators/Indicators.rdf version of this ontology was
      modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20190901/Indicators/Indicators.rdf version of this ontology was
      modified to eliminate a redundant superclass declaration on MarketSpread, introduced by refactoring of FND analytics.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20200401/Indicators/Indicators.rdf version of this ontology was
      modified to reflect the move of dated collection from arrangements to financial dates.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20200701/Indicators/Indicators.rdf version of this ontology was
      modified to add definitions for historical and implied volatility, and differentiate price volatility accordingly.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20210301/Indicators/Indicators.rdf version of this ontology was
      modified to a restriction on isValueOf to MarketRate and eliminate its dependence on PublishedFinancialInformation,
      and to revise the definition of market rate, daily average market rate, and end of day market rate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20210501/Indicators/Indicators.rdf version of this ontology was
      modified to extend the definition of price structure to include a synonym of price history and state that it is intended
      to be used for any sort of analysis of historic prices.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20220801/Indicators/Indicators.rdf version of this ontology was
      modified to loosen the nature of a price in a price structure to include any price, not limited to a quoted price from
      a specific source, to allow for calculated prices to be included in the structure and to deprecate redundant terms including
      financial information publisher, and published financial information.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20221001/Indicators/Indicators.rdf version of the ontology was
      modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata
      vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/Indicators/Indicators.rdf version of this ontology was
      modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating
      redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230301/Indicators/Indicators.rdf version of the ontology was
      modified to eliminate deprecations that are more than 6 months old and to replace content that is now available in the
      OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20231201/Indicators/Indicators.rdf version of the ontology was
      modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20250301/Indicators/Indicators.rdf version of the ontology was
      modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/Organizations/FormalOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/
  - concept: /concepts/fibo/FND/Utilities/Analytics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/20250701/Indicators/Indicators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: Indicators Ontology
type: Ontology Definition
---

# Indicators Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/>

## Relationships

- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [FormalOrganizations](/concepts/fibo/FND/Organizations/FormalOrganizations.md)
- **Related to**: [Analytics](/concepts/fibo/FND/Utilities/Analytics.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [Indicators](<https://spec.edmcouncil.org/fibo/ontology/IND/20250701/Indicators/Indicators/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides the concepts common to all market rates, indices and indicators; that is concepts descriptive of the numeric parameters themselves. These are modeled independently of the values they may take over time.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Indicators Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20140601/Indicators/Indicators.rdf version of this ontology was modified per the issue resolutions identified in the FIBO IND 1.0 FTF 1 report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20160801/Indicators/Indicators.rdf version of this ontology was modified per the FIBO 2.0 RFC, namely, to integrate concepts recently added to the FND domain including Rate, ExchangeRate, InterestRate and StructuredCollection and revise definitions of TermStructure and Volatility to better support concepts such as yield curves and analysis of market rates generally.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20180801/Indicators/Indicators.rdf version of this ontology was modified to integrate the composite date value and reflect migration of statistical measures to Analytics.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20190501/Indicators/Indicators.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20190901/Indicators/Indicators.rdf version of this ontology was modified to eliminate a redundant superclass declaration on MarketSpread, introduced by refactoring of FND analytics.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20200401/Indicators/Indicators.rdf version of this ontology was modified to reflect the move of dated collection from arrangements to financial dates.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20200701/Indicators/Indicators.rdf version of this ontology was modified to add definitions for historical and implied volatility, and differentiate price volatility accordingly.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20210301/Indicators/Indicators.rdf version of this ontology was modified to a restriction on isValueOf to MarketRate and eliminate its dependence on PublishedFinancialInformation, and to revise the definition of market rate, daily average market rate, and end of day market rate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20210501/Indicators/Indicators.rdf version of this ontology was modified to extend the definition of price structure to include a synonym of price history and state that it is intended to be used for any sort of analysis of historic prices.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20220801/Indicators/Indicators.rdf version of this ontology was modified to loosen the nature of a price in a price structure to include any price, not limited to a quoted price from a specific source, to allow for calculated prices to be included in the structure and to deprecate redundant terms including financial information publisher, and published financial information.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20221001/Indicators/Indicators.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/Indicators/Indicators.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230301/Indicators/Indicators.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20231201/Indicators/Indicators.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20250301/Indicators/Indicators.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
- **copyright**: Copyright (c) 2014-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2014-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
