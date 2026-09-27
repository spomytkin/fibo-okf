---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts that are common to derivatives based on variation in some defined variable, such
      as an economic rate, an interest rate or an index value.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2016-2025 EDM Council, Inc.\nCopyright (c) 2016-2025 Object Management Group, Inc.\n\nPermission\
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
    value: Rate Derivatives Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20180801/RateDerivatives/RateDerivatives.rdf version of this
      ontology was extended to include foreign exchange rates, forward rate agreements, and revise definitions to be unambiguous
      and ISO 704 compliant.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20201201/RateDerivatives/RateDerivatives.rdf version of this
      ontology was modified to eliminate the dependency on NonPhysicalUnderlier, which was redundant.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20210801/RateDerivatives/RateDerivatives.rdf version of this
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary, to move the definition of an underlier and the related property, has underlier, to financial instruments
      so that these concepts are also available for use in relation to pool-backed securities.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20230201/RateDerivatives/RateDerivatives.rdf version of this
      ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20240101/RateDerivatives/RateDerivatives.rdf version of this
      ontology was modified to deprecate ForeignExchangeRateObservable after other changes that eliminated its usage in currency
      derivatives and made it obsolete (DER-143).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20240901/RateDerivatives/RateDerivatives.rdf version of this
      ontology was modified to simplify and refine definitions related to underliers (DER-112).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/DER/20250301/RateDerivatives/RateDerivatives.rdf version of this
      ontology was modified to further simplify and clarify definitions (DER-90). Note that under DER-90, the remaining terms
      that were in this ontology have moved to Derivatives Basics, and this ontology will be eliminated when the deprecated
      elements are eliminated (at least 6 months from 4/2025).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/20250401/RateDerivatives/RateDerivatives/
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/RateDerivatives/
sources:
- id: fibo-source-2fb3ec12b8
  resource: references/fibo/DER/RateDerivatives/RateDerivatives.rdf
  sha256: 2fb3ec12b8d9df43db981281e1b2d797aabc54c1b8a9387e4c4b456c709f477d
  title: FIBO source DER/RateDerivatives/RateDerivatives.rdf
title: Rate Derivatives Ontology
type: Ontology Definition
---

# Rate Derivatives Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/RateDerivatives/>

## Relationships

- **Related to**: [DerivativesBasics](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [RateDerivatives](<https://spec.edmcouncil.org/fibo/ontology/DER/20250401/RateDerivatives/RateDerivatives/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts that are common to derivatives based on variation in some defined variable, such as an economic rate, an interest rate or an index value.
- **license**: Copyright (c) 2016-2025 EDM Council, Inc. Copyright (c) 2016-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **label**: Rate Derivatives Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20180801/RateDerivatives/RateDerivatives.rdf version of this ontology was extended to include foreign exchange rates, forward rate agreements, and revise definitions to be unambiguous and ISO 704 compliant.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20201201/RateDerivatives/RateDerivatives.rdf version of this ontology was modified to eliminate the dependency on NonPhysicalUnderlier, which was redundant.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20210801/RateDerivatives/RateDerivatives.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary, to move the definition of an underlier and the related property, has underlier, to financial instruments so that these concepts are also available for use in relation to pool-backed securities.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20230201/RateDerivatives/RateDerivatives.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20240101/RateDerivatives/RateDerivatives.rdf version of this ontology was modified to deprecate ForeignExchangeRateObservable after other changes that eliminated its usage in currency derivatives and made it obsolete (DER-143).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20240901/RateDerivatives/RateDerivatives.rdf version of this ontology was modified to simplify and refine definitions related to underliers (DER-112).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/DER/20250301/RateDerivatives/RateDerivatives.rdf version of this ontology was modified to further simplify and clarify definitions (DER-90). Note that under DER-90, the remaining terms that were in this ontology have moved to Derivatives Basics, and this ontology will be eliminated when the deprecated elements are eliminated (at least 6 months from 4/2025).
- **copyright**: Copyright (c) 2016-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2016-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
