---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts related to parametric schedules, including how to represent individual schedules
      as well as related date periods, explicit dates, and other concepts needed for parametric schedule representation.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2016-2025 EDM Council, Inc.\nCopyright (c) 2018-2025 Object Management Group, Inc.\n\nPermission\
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
    value: Parametric Schedules Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20180801/Securities/ParametricSchedules.rdf version of this ontology
      was modified to rename (migrate) the hasDefinition property to isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190701/Securities/ParametricSchedules.rdf version of this ontology
      was modified to eliminate circular definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210201/Securities/ParametricSchedules.rdf version of this ontology
      was modified to address text formatting hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Securities/ParametricSchedules.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Securities/ParametricSchedules.rdf version of this ontology
      was modified to move the property, 'is conferred on' to the Legal Capacity ontology and to use the Commons Ontology
      Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Securities/ParametricSchedules.rdf version of this ontology
      was modified to move certain very general concepts related to calculation dates and events to FND and to integrate concepts
      related to scheduled interest rate related events that were previously embedded in DER to make them available for broader
      use.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240301/Securities/ParametricSchedules.rdf version of this ontology
      was modified to eliminate a hygiene issue related to parametric schedule.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240601/Securities/ParametricSchedules.rdf version of this ontology
      was modified to eliminate elements that have been deprecated over six months (FND-386).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20241101/Securities/ParametricSchedules.rdf version of this ontology
      was modified to better classify the concept of a floating-rate note date rule (SEC-150).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/20250201/Securities/ParametricSchedules/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: Parametric Schedules Ontology
type: Ontology Definition
---

# Parametric Schedules Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/>

## Relationships

- **Related to**: [BusinessDates](/concepts/fibo/FND/DatesAndTimes/BusinessDates.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Occurrences](/concepts/fibo/FND/DatesAndTimes/Occurrences.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [ParametricSchedules](<https://spec.edmcouncil.org/fibo/ontology/SEC/20250201/Securities/ParametricSchedules/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts related to parametric schedules, including how to represent individual schedules as well as related date periods, explicit dates, and other concepts needed for parametric schedule representation.
- **license**: Copyright (c) 2016-2025 EDM Council, Inc. Copyright (c) 2018-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **label**: Parametric Schedules Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20180801/Securities/ParametricSchedules.rdf version of this ontology was modified to rename (migrate) the hasDefinition property to isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190701/Securities/ParametricSchedules.rdf version of this ontology was modified to eliminate circular definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210201/Securities/ParametricSchedules.rdf version of this ontology was modified to address text formatting hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220801/Securities/ParametricSchedules.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Securities/ParametricSchedules.rdf version of this ontology was modified to move the property, 'is conferred on' to the Legal Capacity ontology and to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Securities/ParametricSchedules.rdf version of this ontology was modified to move certain very general concepts related to calculation dates and events to FND and to integrate concepts related to scheduled interest rate related events that were previously embedded in DER to make them available for broader use.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240301/Securities/ParametricSchedules.rdf version of this ontology was modified to eliminate a hygiene issue related to parametric schedule.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240601/Securities/ParametricSchedules.rdf version of this ontology was modified to eliminate elements that have been deprecated over six months (FND-386).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20241101/Securities/ParametricSchedules.rdf version of this ontology was modified to better classify the concept of a floating-rate note date rule (SEC-150).
- **copyright**: Copyright (c) 2016-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2018-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
