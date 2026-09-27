---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides reference data for commonly referenced interest rates, specifically those that are referenced
      in the ISDA FpML codes for floating interest rates. The rates included herein are generated directly from the FpML published
      reference data.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2015-2025 Object Management Group,\
      \ Inc.\nCopyright (c) 2015-2026 Thematix Partners LLC\nCopyright (c) 2023-2026 Federated Knowledge, LLC\n\nPermission\
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
    value: Common Interest Rates Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20190101/InterestRates/InterestRates.rdf version of this ontology
      was revised extensively to restructure the way in which interest rate benchmarks are modeled and eliminate references
      to the merged interest rate publishers ontology.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20190101/InterestRates/InterestRates.rdf version of this ontology
      was revised to reflect the latest FpML rates.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20210301/InterestRates/InterestRates.rdf version of this ontology
      was revised to reflect the latest FpML rates, which include a number of changes, including deprecating some rates and
      replacing them with others.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20211201/InterestRates/CommonInterestRates.rdf version of the
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/InterestRates/InterestRates.rdf version of this ontology
      was modified to normalize the prefix for the EU individuals ontology and update the reference interest rates as of 10
      March 2023.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20230601/InterestRates/InterestRates.rdf version of this ontology
      was modified to normalize the prefix for the EU individuals ontology and update the reference interest rates as of 26
      April 2024.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20240601/InterestRates/InterestRates.rdf version of this ontology
      was modified to update the reference interest rates as of Q4 2024.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20241201/InterestRates/InterestRates.rdf version of the ontology
      was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2
      (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/IND/20250301/InterestRates/InterestRates.rdf version of the ontology
      was modified to reflect migration of some registration authorities in FBC (FND-407).
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.fpml.org/coding-scheme/floating-rate-index-3-10.xml
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2026 Thematix Partners LLC
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2023-2026 Federated Knowledge, LLC
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/
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
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/20260601/InterestRates/CommonInterestRates/
  - concept: /concepts/fibo/IND/InterestRates/InterestRates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/
  - concept: /concepts/fibo/IND/InterestRates/MarketDataProviders.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/
sources:
- id: fibo-source-8e1390b32c
  resource: references/fibo/IND/InterestRates/CommonInterestRates.rdf
  sha256: 8e1390b32c1121edb492a0eee451b982bac6fbbed762aec6a29cd52950b5b0b2
  title: FIBO source IND/InterestRates/CommonInterestRates.rdf
title: Common Interest Rates Ontology
type: Ontology Definition
---

# Common Interest Rates Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/CommonInterestRates/>

## Relationships

- **Related to**: [CommercialRegistrationAuthorities](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md)
- **Related to**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **Related to**: [ISO4217-CurrencyCodes](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [InterestRates](/concepts/fibo/IND/InterestRates/InterestRates.md)
- **Related to**: [MarketDataProviders](/concepts/fibo/IND/InterestRates/MarketDataProviders.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [CommonInterestRates](<https://spec.edmcouncil.org/fibo/ontology/IND/20260601/InterestRates/CommonInterestRates/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides reference data for commonly referenced interest rates, specifically those that are referenced in the ISDA FpML codes for floating interest rates. The rates included herein are generated directly from the FpML published reference data.
- **license**: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc. Copyright (c) 2015-2026 Thematix Partners LLC Copyright (c) 2023-2026 Federated Knowledge, LLC  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Common Interest Rates Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20190101/InterestRates/InterestRates.rdf version of this ontology was revised extensively to restructure the way in which interest rate benchmarks are modeled and eliminate references to the merged interest rate publishers ontology.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20190101/InterestRates/InterestRates.rdf version of this ontology was revised to reflect the latest FpML rates.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20210301/InterestRates/InterestRates.rdf version of this ontology was revised to reflect the latest FpML rates, which include a number of changes, including deprecating some rates and replacing them with others.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20211201/InterestRates/CommonInterestRates.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230201/InterestRates/InterestRates.rdf version of this ontology was modified to normalize the prefix for the EU individuals ontology and update the reference interest rates as of 10 March 2023.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20230601/InterestRates/InterestRates.rdf version of this ontology was modified to normalize the prefix for the EU individuals ontology and update the reference interest rates as of 26 April 2024.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20240601/InterestRates/InterestRates.rdf version of this ontology was modified to update the reference interest rates as of Q4 2024.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20241201/InterestRates/InterestRates.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/IND/20250301/InterestRates/InterestRates.rdf version of the ontology was modified to reflect migration of some registration authorities in FBC (FND-407).
- **adaptedFrom**: http://www.fpml.org/coding-scheme/floating-rate-index-3-10.xml
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2015-2026 EDM Association dba EDM Council, Inc.
- **copyright**: Copyright (c) 2015-2026 Thematix Partners LLC
- **copyright**: Copyright (c) 2023-2026 Federated Knowledge, LLC

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
