---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides scaffolding for use in describing concepts related to facilities, both virtual and physical,
      including physical sites that provide various facilities.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\n\t\tCopyright (c) 2013-2025 Object Management Group, Inc.\n\t\t\n\t\
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
    value: Facilities Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Places/Facilities.rdf version of this ontology was modified
      for the FIBO 2.0 RFC to integrate it with LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20180801/Places/Facilities.rdf version of this ontology was modified
      to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20190901/Places/Facilities.rdf version of this ontology was modified
      to eliminate circular and ambiguous definitions, and simplify the ontology by merging physical site with site.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20210101/Places/Facilities.rdf version of this ontology was modified
      to allow a facility to exist at some location that has an address without requiring it to be situated at some site to
      simplify usage in cases where the site and facility have 100 percent overlap and are not tracked independently.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20220101/Places/Facilities.rdf version of this ontology was modified
      to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20220701/Places/Facilities.rdf version of this ontology was modified
      to allow a facility to be anything rather than a role.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20221201/Places/Facilities.rdf version of the ontology was modified
      to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Places/Facilities.rdf version of this ontology was modified
      to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating
      redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Places/Facilities.rdf version of this ontology was modified
      to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Places/Facilities.rdf version of this ontology was modified
      to integrate with the new real property ontology (LOAN-168).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241001/Places/Facilities.rdf version of the ontology was modified
      to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Places/Facilities.rdf version of the ontology was modified
      to eliminate long deprecated elements (FND-399), and to reuse concepts from the Commons 1.3 sites and facilities ontology
      (FND-401). Note that this ontology will be eliminated in its entirety sometime after the Q3 2026 release of FIBO given
      that all of its content has been deprecated.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: This ontology was added to Foundations in advance of the December 2014 Long Beach meeting in support of the SEC
      specification.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20251201/Places/Facilities/
  - concept: /concepts/fibo/FND/Places/Addresses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/
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
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/SitesAndFacilities/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Facilities/
sources:
- id: fibo-source-1e7f45e6e0
  resource: references/fibo/FND/Places/Facilities.rdf
  sha256: 1e7f45e6e0c3362eab2edc0e2989e42e7930b2d62abb45ddcf484a9cc8a64965
  title: FIBO source FND/Places/Facilities.rdf
title: Facilities Ontology
type: Ontology Definition
---

# Facilities Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Facilities/>

## Relationships

- **Related to**: [Addresses](/concepts/fibo/FND/Places/Addresses.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [SitesAndFacilities](<https://www.omg.org/spec/Commons/SitesAndFacilities/>)
- **Related to**: [Facilities](<https://spec.edmcouncil.org/fibo/ontology/FND/20251201/Places/Facilities/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides scaffolding for use in describing concepts related to facilities, both virtual and physical, including physical sites that provide various facilities.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. 		Copyright (c) 2013-2025 Object Management Group, Inc. 		 		Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Facilities Ontology
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Places/Facilities.rdf version of this ontology was modified for the FIBO 2.0 RFC to integrate it with LCC.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20180801/Places/Facilities.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20190901/Places/Facilities.rdf version of this ontology was modified to eliminate circular and ambiguous definitions, and simplify the ontology by merging physical site with site.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20210101/Places/Facilities.rdf version of this ontology was modified to allow a facility to exist at some location that has an address without requiring it to be situated at some site to simplify usage in cases where the site and facility have 100 percent overlap and are not tracked independently.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20220101/Places/Facilities.rdf version of this ontology was modified to address hygiene issues with respect to text formatting.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20220701/Places/Facilities.rdf version of this ontology was modified to allow a facility to be anything rather than a role.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20221201/Places/Facilities.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Places/Facilities.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Places/Facilities.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Places/Facilities.rdf version of this ontology was modified to integrate with the new real property ontology (LOAN-168).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241001/Places/Facilities.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Places/Facilities.rdf version of the ontology was modified to eliminate long deprecated elements (FND-399), and to reuse concepts from the Commons 1.3 sites and facilities ontology (FND-401). Note that this ontology will be eliminated in its entirety sometime after the Q3 2026 release of FIBO given that all of its content has been deprecated.
- **changeNote**: This ontology was added to Foundations in advance of the December 2014 Long Beach meeting in support of the SEC specification.
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
