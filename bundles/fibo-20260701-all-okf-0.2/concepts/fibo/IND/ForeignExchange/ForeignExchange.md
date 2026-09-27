---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides the parameters for foreign exchange rates, covering spot and forward rates, as well as foreign
      exchange spot rate volatilities.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2014-2025 EDM Council, Inc.\nCopyright (c) 2014-2025 Object Management Group, Inc.\n\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\nSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Foreign Exchange Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20140601/ForeignExchange/ForeignExchange.rdf version of this
      ontology was modified per the issue resolutions identified in the FIBO IND 1.0 FTF 1 report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20150501/ForeignExchange/ForeignExchange.rdf version of this
      ontology was modified per the issue resolutions identified in the FIBO IND 1.0 FTF 2 report, namely, to take advantage
      of content added via the FIBO FND 1.1 with respect to higher-level concepts of Rate, ExchangeRate, and InterestRate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20160801/ForeignExchange/ForeignExchange.rdf version of this
      ontology was modified per the FIBO 2.0 RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20180801/ForeignExchange/ForeignExchange.rdf version of this
      ontology was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20190901/ForeignExchange/ForeignExchange.rdf version of this
      ontology was modified to eliminate unnecessary references, some of which had incorrect datatypes, rename FxSpotVolatility
      to CurrencySpotVolatility and improve its definition and related volatility definitions more generally.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20210301/ForeignExchange/ForeignExchange.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/ForeignExchange/ForeignExchange.rdf version of this
      ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes
      (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230301/ForeignExchange/ForeignExchange.rdf version of this
      ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20231201/ForeignExchange/ForeignExchange.rdf version of this
      ontology was modified to add the source for a quoted exchange rate (DER-143).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20240801/ForeignExchange/ForeignExchange.rdf version of the ontology
      was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/20250701/ForeignExchange/ForeignExchange/
  - concept: /concepts/fibo/IND/Indicators/Indicators.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: Foreign Exchange Ontology
type: Ontology Definition
---

# Foreign Exchange Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/>

## Relationships

- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [Markets](/concepts/fibo/FBC/FunctionalEntities/Markets.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [Indicators](/concepts/fibo/IND/Indicators/Indicators.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [ForeignExchange](<https://spec.edmcouncil.org/fibo/ontology/IND/20250701/ForeignExchange/ForeignExchange/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides the parameters for foreign exchange rates, covering spot and forward rates, as well as foreign exchange spot rate volatilities.
- **license**: Copyright (c) 2014-2025 EDM Council, Inc. Copyright (c) 2014-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **label**: Foreign Exchange Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20140601/ForeignExchange/ForeignExchange.rdf version of this ontology was modified per the issue resolutions identified in the FIBO IND 1.0 FTF 1 report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20150501/ForeignExchange/ForeignExchange.rdf version of this ontology was modified per the issue resolutions identified in the FIBO IND 1.0 FTF 2 report, namely, to take advantage of content added via the FIBO FND 1.1 with respect to higher-level concepts of Rate, ExchangeRate, and InterestRate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20160801/ForeignExchange/ForeignExchange.rdf version of this ontology was modified per the FIBO 2.0 RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20180801/ForeignExchange/ForeignExchange.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20190901/ForeignExchange/ForeignExchange.rdf version of this ontology was modified to eliminate unnecessary references, some of which had incorrect datatypes, rename FxSpotVolatility to CurrencySpotVolatility and improve its definition and related volatility definitions more generally.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20210301/ForeignExchange/ForeignExchange.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/ForeignExchange/ForeignExchange.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230301/ForeignExchange/ForeignExchange.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20231201/ForeignExchange/ForeignExchange.rdf version of this ontology was modified to add the source for a quoted exchange rate (DER-143).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20240801/ForeignExchange/ForeignExchange.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
- **copyright**: Copyright (c) 2014-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2014-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
