---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology refines the notion of a business center for reference in defining markets and exchanges, clearing
      houses, and other functional entities as appropriate. The ontology covers the concept of an FpML business center (excluding
      those that are business day adjustments), with a focus on a physical place where business is transacted, where relevant.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2018-2025 EDM Council, Inc.\n\t\tCopyright (c) 2018-2025 Object Management Group, Inc.\n\t\t\n\t\
      \tPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation\
      \ files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use,\
      \ copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to\
      \ whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this\
      \ permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED\
      \ 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Business Centers Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180901/FunctionalEntities/BusinessCenters.rdf version of this
      ontology was revised to eliminate duplication with concepts in LCC and to merge countries with locations.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/FunctionalEntities/BusinessCenters.rdf version of this
      ontology was revised to eliminate circular imports and make definitions ISO 704 compliant.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200901/FunctionalEntities/BusinessCenters.rdf version of this
      ontology was revised to address text formatting issues uncovered by hygiene testing.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FunctionalEntities/BusinessCenters.rdf version of the
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/BusinessCenters.rdf version of this
      ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes
      (LCC) and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FunctionalEntities/BusinessCenters.rdf version of the
      ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/BusinessCenters/
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/
sources:
- id: fibo-source-9bbbd18083
  resource: references/fibo/FBC/FunctionalEntities/BusinessCenters.rdf
  sha256: 9bbbd18083fbf3183af8c86eb613aa661a0110b3c02acb42c40459b17aaefe20
  title: FIBO source FBC/FunctionalEntities/BusinessCenters.rdf
title: Business Centers Ontology
type: Ontology Definition
---

# Business Centers Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/>

## Relationships

- **Related to**: [BusinessDates](/concepts/fibo/FND/DatesAndTimes/BusinessDates.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [CodesAndCodeSets](<https://www.omg.org/spec/Commons/CodesAndCodeSets/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [BusinessCenters](<https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/BusinessCenters/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology refines the notion of a business center for reference in defining markets and exchanges, clearing houses, and other functional entities as appropriate. The ontology covers the concept of an FpML business center (excluding those that are business day adjustments), with a focus on a physical place where business is transacted, where relevant.
- **license**: Copyright (c) 2018-2025 EDM Council, Inc. 		Copyright (c) 2018-2025 Object Management Group, Inc. 		 		Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Business Centers Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180901/FunctionalEntities/BusinessCenters.rdf version of this ontology was revised to eliminate duplication with concepts in LCC and to merge countries with locations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/FunctionalEntities/BusinessCenters.rdf version of this ontology was revised to eliminate circular imports and make definitions ISO 704 compliant.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200901/FunctionalEntities/BusinessCenters.rdf version of this ontology was revised to address text formatting issues uncovered by hygiene testing.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FunctionalEntities/BusinessCenters.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/BusinessCenters.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FunctionalEntities/BusinessCenters.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2018-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2018-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
