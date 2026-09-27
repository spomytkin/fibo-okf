---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides definitions of date and schedule concepts for use in other FIBO ontologies.
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
    value: Financial Dates Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/DatesAndTimes/FinancialDates/ version of this ontology
      was revised by the FIBO FND 1.2 RTF in order to introduce the definition of a time interval, which is a location, to
      ground some of the concepts such as a date period, and duration as well as to support the definition of business recurrence
      intervals for use in parametric schedules for securities.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20170201/DatesAndTimes/FinancialDates/ version of this ontology
      was revised by the FIBO 2.0 RFC in order to introduce the definition of a time instant, to eliminate a reasoning issue
      with relative dates, and remove a circular dependency inadvertently incorporated in the ontology with a FIBO FND 1.2
      modification.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/DatesAndTimes/FinancialDates/ version of this ontology
      was revised to introduce a composite date datatype to allow for cases whereby the representation of a date for certain
      purposes, such as GLEIF LEI data, is inconsistent, and to facilitate mapping FIBO to multiple data sources in user environments.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190201/DatesAndTimes/FinancialDates/ version of this ontology
      was revised to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/DatesAndTimes/FinancialDates/ version of this ontology
      was revised to add the 'has date added' property, which is needed for the date a constituent is added to a basket, among
      other purposes, to add a TimeOfDay class, needed for representing rate reset times, eliminate duplication with concepts
      in LCC, and make AdHocScheduleEntry a child of DatedCollectionConstituent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/DatesAndTimes/FinancialDates/ version of this ontology
      was revised to move dated collection and dated collection constituent as well as hasObservedDateTime and hasAcquisitionDate
      to financial dates in order to improve usability, simplify reasoning, made definitions ISO 704 compliant, and eliminate
      redundant restrictions on ad hoc schedule entry.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/DatesAndTimes/FinancialDates/ version of this ontology
      was revised to add hasOpeningDateTime and hasClosingDateTime for use in defining trading days and sessions and eliminated
      the functional property declaration on hasExplicitDate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/DatesAndTimes/FinancialDates/ version of this ontology
      was revised to add the concept of age and a corresponding property that supports its use.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/DatesAndTimes/FinancialDates.rdf version of this ontology
      was modified to add notes on the custom CombinedDateTime datatype indicating that it is outside the RL profile and that
      if someone wants to use this ontology with OWL 2 RL rules they might want to comment this out / eliminate it where it
      is used.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210901/DatesAndTimes/FinancialDates.rdf version of this ontology
      was modified to remove a functional declaration on hasObservedDateTime, which causes reasoning inconsistencies when
      there are multiple uses of that property for certain individuals, such as for LEI registration.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/DatesAndTimes/FinancialDates.rdf version of this ontology
      was modified to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/DatesAndTimes/FinancialDates.rdf version of the ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/DatesAndTimes/FinancialDates.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC),
      eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/DatesAndTimes/FinancialDates.rdf version of the ontology
      was modified to eliminate deprecations that are more than 6 months old.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/DatesAndTimes/FinancialDates.rdf version of the ontology
      was modified to add the general notions of explicit anchor date and calculation period (FBC-317) and to add the concept
      of a business calendar (FBC-319).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240301/DatesAndTimes/FinancialDates.rdf version of the ontology
      was modified to eliminate elements that have been deprecated for several quarters (FND-386).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/DatesAndTimes/FinancialDates.rdf version of the ontology
      was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
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
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20250701/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: Financial Dates Ontology
type: Ontology Definition
---

# Financial Dates Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [FinancialDates](<https://spec.edmcouncil.org/fibo/ontology/FND/20250701/DatesAndTimes/FinancialDates/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides definitions of date and schedule concepts for use in other FIBO ontologies.
- **license**: Copyright (c) 2014-2025 EDM Council, Inc. Copyright (c) 2014-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **label**: Financial Dates Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/DatesAndTimes/FinancialDates/ version of this ontology was revised by the FIBO FND 1.2 RTF in order to introduce the definition of a time interval, which is a location, to ground some of the concepts such as a date period, and duration as well as to support the definition of business recurrence intervals for use in parametric schedules for securities.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20170201/DatesAndTimes/FinancialDates/ version of this ontology was revised by the FIBO 2.0 RFC in order to introduce the definition of a time instant, to eliminate a reasoning issue with relative dates, and remove a circular dependency inadvertently incorporated in the ontology with a FIBO FND 1.2 modification.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/DatesAndTimes/FinancialDates/ version of this ontology was revised to introduce a composite date datatype to allow for cases whereby the representation of a date for certain purposes, such as GLEIF LEI data, is inconsistent, and to facilitate mapping FIBO to multiple data sources in user environments.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190201/DatesAndTimes/FinancialDates/ version of this ontology was revised to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/DatesAndTimes/FinancialDates/ version of this ontology was revised to add the 'has date added' property, which is needed for the date a constituent is added to a basket, among other purposes, to add a TimeOfDay class, needed for representing rate reset times, eliminate duplication with concepts in LCC, and make AdHocScheduleEntry a child of DatedCollectionConstituent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/DatesAndTimes/FinancialDates/ version of this ontology was revised to move dated collection and dated collection constituent as well as hasObservedDateTime and hasAcquisitionDate to financial dates in order to improve usability, simplify reasoning, made definitions ISO 704 compliant, and eliminate redundant restrictions on ad hoc schedule entry.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/DatesAndTimes/FinancialDates/ version of this ontology was revised to add hasOpeningDateTime and hasClosingDateTime for use in defining trading days and sessions and eliminated the functional property declaration on hasExplicitDate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/DatesAndTimes/FinancialDates/ version of this ontology was revised to add the concept of age and a corresponding property that supports its use.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/DatesAndTimes/FinancialDates.rdf version of this ontology was modified to add notes on the custom CombinedDateTime datatype indicating that it is outside the RL profile and that if someone wants to use this ontology with OWL 2 RL rules they might want to comment this out / eliminate it where it is used.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210901/DatesAndTimes/FinancialDates.rdf version of this ontology was modified to remove a functional declaration on hasObservedDateTime, which causes reasoning inconsistencies when there are multiple uses of that property for certain individuals, such as for LEI registration.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/DatesAndTimes/FinancialDates.rdf version of this ontology was modified to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/DatesAndTimes/FinancialDates.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/DatesAndTimes/FinancialDates.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/DatesAndTimes/FinancialDates.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/DatesAndTimes/FinancialDates.rdf version of the ontology was modified to add the general notions of explicit anchor date and calculation period (FBC-317) and to add the concept of a business calendar (FBC-319).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240301/DatesAndTimes/FinancialDates.rdf version of the ontology was modified to eliminate elements that have been deprecated for several quarters (FND-386).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/DatesAndTimes/FinancialDates.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
- **changeNote**: This ontology was added to Foundations in advance of the December 2014 Long Beach meeting in support of the SEC specification. It is also needed to provide temporal relationships for Ownership and Control.  These three ontologies are designed for use together:  	* FinancialDates -- financial Dates and Schedules 	* BusinessDates -- business day adjustments 	* Occurrences -- occurrences (events) and kinds of occurrences  They are modularized this way to minimize the ontological committments that are imposed upon ontologies that rely upon them. Ontologies can import FinancialDates alone, or FinancialDates + BusinessDates, or FinancialDates + Occurrences, or all three together.
- **copyright**: Copyright (c) 2014-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2014-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
