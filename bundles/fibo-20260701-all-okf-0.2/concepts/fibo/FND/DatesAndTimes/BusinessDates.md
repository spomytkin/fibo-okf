---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology extends definitions of date and schedule concepts from the FinancialDates ontology with concepts
      defining dates that may be adjusted when they fall on weekends or holidays as defined in a given business center, for
      use in other FIBO ontologies.
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
    value: Business Dates Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/DatesAndTimes/BusinessDates/ version of this ontology
      was revised by the FIBO FND 1.2 RTF in order to add definitions for business recurrence intervals such as the day of
      the month and week, and to revise the representation of the end of the month to correspond to the way that the other
      intervals are represented for use in parametric schedules.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/DatesAndTimes/BusinessDates/ version of this ontology
      was revised to better support definitions related to business day adjustments.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180901/DatesAndTimes/BusinessDates/ version of this ontology
      was revised to loosen domains on properties related to business day and day count (recurrence interval) conventions,
      eliminate a duplicate individual, normalize definitions to be ISO 704 compliant, eliminate duplication of concepts in
      LCC, move hasBusinessCenter to locations, where the class BusinessCenter is defined and merge countries with locations.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/DatesAndTimes/BusinessDates/ version of this ontology
      was revised to eliminate a remaining circular definition.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/DatesAndTimes/BusinessDates/ version of this ontology
      was revised to address hygiene issues with respect to text processing.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/DatesAndTimes/BusinessDates.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/DatesAndTimes/BusinessDates.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC),
      eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/DatesAndTimes/BusinessDates.rdf version of this ontology
      was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/DatesAndTimes/BusinessDates.rdf version of this ontology
      was modified to eliminate elements that have been deprecated for several quarters (FND-386).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/DatesAndTimes/BusinessDates.rdf version of this ontology
      was modified to reconcile business day adjustments with business day conventions, which are synonymous (SEC-150).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250201/DatesAndTimes/BusinessDates.rdf version of the ontology
      was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2
      (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/DatesAndTimes/BusinessDates.rdf version of the ontology
      was modified to eliminate deprecations that were more than 3 quarters old (FND-399).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "This ontology was added to Foundations in advance of the December 2014 Long Beach meeting in support of the SEC\
      \ specification. It is also needed to provide temporal relationships for Ownership and Control.\n\nThese three ontologies\
      \ are designed for use together:\n\n\t* FinancialDates -- financial Dates and Schedules\n\t* BusinessDates -- business\
      \ day adjustments\n\t* Occurrences -- occurrences (events) and kinds of occurrences\n\nThey are modularized this way\
      \ to minimize the ontological committments that are imposed upon ontologies that rely upon them. Ontologies can import\
      \ FinancialDates alone, or FinancialDates + BusinessDates, or FinancialDates + Occurrences, or all three together."
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2014-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20251201/DatesAndTimes/BusinessDates/
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
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/
sources:
- id: fibo-source-7e287b0092
  resource: references/fibo/FND/DatesAndTimes/BusinessDates.rdf
  sha256: 7e287b0092247d35e3e8e12b9c1c29cba3b2b4f94d06a6b0c06e85f6c1cc2f62
  title: FIBO source FND/DatesAndTimes/BusinessDates.rdf
title: Business Dates Ontology
type: Ontology Definition
---

# Business Dates Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/>

## Relationships

- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [BusinessDates](<https://spec.edmcouncil.org/fibo/ontology/FND/20251201/DatesAndTimes/BusinessDates/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology extends definitions of date and schedule concepts from the FinancialDates ontology with concepts defining dates that may be adjusted when they fall on weekends or holidays as defined in a given business center, for use in other FIBO ontologies.
- **license**: Copyright (c) 2014-2025 EDM Council, Inc. Copyright (c) 2014-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **label**: Business Dates Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/DatesAndTimes/BusinessDates/ version of this ontology was revised by the FIBO FND 1.2 RTF in order to add definitions for business recurrence intervals such as the day of the month and week, and to revise the representation of the end of the month to correspond to the way that the other intervals are represented for use in parametric schedules.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/DatesAndTimes/BusinessDates/ version of this ontology was revised to better support definitions related to business day adjustments.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180901/DatesAndTimes/BusinessDates/ version of this ontology was revised to loosen domains on properties related to business day and day count (recurrence interval) conventions, eliminate a duplicate individual, normalize definitions to be ISO 704 compliant, eliminate duplication of concepts in LCC, move hasBusinessCenter to locations, where the class BusinessCenter is defined and merge countries with locations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/DatesAndTimes/BusinessDates/ version of this ontology was revised to eliminate a remaining circular definition.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/DatesAndTimes/BusinessDates/ version of this ontology was revised to address hygiene issues with respect to text processing.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/DatesAndTimes/BusinessDates.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/DatesAndTimes/BusinessDates.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/DatesAndTimes/BusinessDates.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/DatesAndTimes/BusinessDates.rdf version of this ontology was modified to eliminate elements that have been deprecated for several quarters (FND-386).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/DatesAndTimes/BusinessDates.rdf version of this ontology was modified to reconcile business day adjustments with business day conventions, which are synonymous (SEC-150).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250201/DatesAndTimes/BusinessDates.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/DatesAndTimes/BusinessDates.rdf version of the ontology was modified to eliminate deprecations that were more than 3 quarters old (FND-399).
- **changeNote**: This ontology was added to Foundations in advance of the December 2014 Long Beach meeting in support of the SEC specification. It is also needed to provide temporal relationships for Ownership and Control.  These three ontologies are designed for use together:  	* FinancialDates -- financial Dates and Schedules 	* BusinessDates -- business day adjustments 	* Occurrences -- occurrences (events) and kinds of occurrences  They are modularized this way to minimize the ontological committments that are imposed upon ontologies that rely upon them. Ontologies can import FinancialDates alone, or FinancialDates + BusinessDates, or FinancialDates + Occurrences, or all three together.
- **copyright**: Copyright (c) 2014-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2014-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
