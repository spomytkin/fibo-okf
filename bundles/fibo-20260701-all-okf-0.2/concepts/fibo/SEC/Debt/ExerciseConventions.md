---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines the various kinds of exercise conventions that are common to debt and options instruments.
      They are distinguished primarily in terms of the date period during which an optional contract clause may be exercised.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2015-2025 EDM Council, Inc.\nCopyright (c) 2015-2025 Object Management Group, Inc.\n\t\t\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Exercise Conventions Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/20211001/Debt/ExerciseConventions.rdf version of the ontology was
      modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata
      vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190101/Debt/ExerciseConventions.rdf version of this ontology
      was added to support integration of Bonds and Options in SEC and DER, respectively.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190101/Debt/ExerciseConventions.rdf version of this ontology
      was modified to add the hasExerciseTerms property.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190501/Debt/ExerciseConventions.rdf version of this ontology
      was modified to eliminate duplication of concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200301/Debt/ExerciseConventions.rdf version of this ontology
      was modified to revise the definition of American exercise terms to say that an option with such terms may be exercised
      on or before the expiration date of the contract.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210901/Debt/ExerciseConventions.rdf version of this ontology
      was modified to loosen the domain of hasExerciseTerms to allow for entitlements to have such terms.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Debt/ExerciseConventions.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC)
      and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Debt/ExerciseConventions.rdf version of the ontology
      was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2
      (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Debt/ExerciseConventions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/
sources:
- id: fibo-source-b0549059cf
  resource: references/fibo/SEC/Debt/ExerciseConventions.rdf
  sha256: b0549059cf085c65a45ceb8097c6a5d1580392da9215ca35ca9afe213b18f5e4
  title: FIBO source SEC/Debt/ExerciseConventions.rdf
title: Exercise Conventions Ontology
type: Ontology Definition
---

# Exercise Conventions Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/>

## Relationships

- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [BusinessDates](/concepts/fibo/FND/DatesAndTimes/BusinessDates.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [ExerciseConventions](<https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Debt/ExerciseConventions/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines the various kinds of exercise conventions that are common to debt and options instruments. They are distinguished primarily in terms of the date period during which an optional contract clause may be exercised.
- **license**: Copyright (c) 2015-2025 EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label** (en): Exercise Conventions Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/20211001/Debt/ExerciseConventions.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190101/Debt/ExerciseConventions.rdf version of this ontology was added to support integration of Bonds and Options in SEC and DER, respectively.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190101/Debt/ExerciseConventions.rdf version of this ontology was modified to add the hasExerciseTerms property.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190501/Debt/ExerciseConventions.rdf version of this ontology was modified to eliminate duplication of concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200301/Debt/ExerciseConventions.rdf version of this ontology was modified to revise the definition of American exercise terms to say that an option with such terms may be exercised on or before the expiration date of the contract.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210901/Debt/ExerciseConventions.rdf version of this ontology was modified to loosen the domain of hasExerciseTerms to allow for entitlements to have such terms.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Debt/ExerciseConventions.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Debt/ExerciseConventions.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2015-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
