---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology tests the high level concept of formal organization used in other FIBO ontology elements.
  - predicate: http://purl.org/dc/terms/contributor
    value: Adaptive Analytics, Inc.
  - predicate: http://purl.org/dc/terms/contributor
    value: Thematix Partners LLC
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\t\
      See https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Formal Organizations Test Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/Organizations/TestFormalOrganizations.rdf version of
      the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230201/Organizations/TestFormalOrganizations.rdf version of
      this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Organizations/TestFormalOrganizations.rdf version of
      the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Organizations/TestFormalOrganizations.rdf version of
      the ontology was modified to replace additional properties that are now available in the OMG Commons Ontology Library
      (Commons) v1.3 (FND-412).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "This version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\
      \   (1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing\
      \ \n   (2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs\n   (3)\
      \ to change the file suffix from .owl to .rdf to increase usability in RDF tools\n   (4) to use 4-level abbreviations\
      \ and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n\
      \   (5) to incorporate changes to the specification metadata to support documentation at the family, specification,\
      \ module, and ontology level, similar to the abbreviations."
  - predicate: http://www.w3.org/2004/02/skos/core#historyNote
    value: "This version of the FIBO Foundations Specification was revised primarily to reflect comments received at the March\
      \ 2013 OMG Technical Meeting in Reston and reflected in the Errata discussed at the June 2013 OMG Technical Meeting\
      \ in Berlin. \n\nRevisions to FIBO Foundations are managed per the process outlined in the Policies and Procedures for\
      \ OMG standards, with the intent to maintain backwards compatibility in the ontologies to the degree possible.\n  \n\
      The RDF/XML serialized OWL for the Foundations ODM/OWL ontologies have been checked for syntactic errors and logical\
      \ consistency with Protege 4 (http://protege.stanford.edu/), HermiT 1.3.7 (http://www.hermit-reasoner.com/) and Pellet\
      \ 2.2 (http://clarkparsia.com/pellet/)."
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Organizations/TestFormalOrganizations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/TestFormalOrganizations/
sources:
- id: fibo-source-551bd52f50
  resource: references/fibo/etc/testing/data/fnd/Organizations/TestFormalOrganizations.rdf
  sha256: 551bd52f50a8c2167cf3054686869d6e0eb5fd5f1052d50778142fed224aedb8
  title: FIBO source etc/testing/data/fnd/Organizations/TestFormalOrganizations.rdf
title: Formal Organizations Test Ontology
type: Ontology Definition
---

# Formal Organizations Test Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/TestFormalOrganizations/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [TestFormalOrganizations](<https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Organizations/TestFormalOrganizations/>)

## Annotations

- **abstract**: This ontology tests the high level concept of formal organization used in other FIBO ontology elements.
- **contributor**: Adaptive Analytics, Inc.
- **contributor**: Thematix Partners LLC
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Formal Organizations Test Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/Organizations/TestFormalOrganizations.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230201/Organizations/TestFormalOrganizations.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Organizations/TestFormalOrganizations.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Organizations/TestFormalOrganizations.rdf version of the ontology was modified to replace additional properties that are now available in the OMG Commons Ontology Library (Commons) v1.3 (FND-412).
- **changeNote**: This version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:    (1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing     (2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs    (3) to change the file suffix from .owl to .rdf to increase usability in RDF tools    (4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure    (5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations.
- **historyNote**: This version of the FIBO Foundations Specification was revised primarily to reflect comments received at the March 2013 OMG Technical Meeting in Reston and reflected in the Errata discussed at the June 2013 OMG Technical Meeting in Berlin.   Revisions to FIBO Foundations are managed per the process outlined in the Policies and Procedures for OMG standards, with the intent to maintain backwards compatibility in the ontologies to the degree possible.    The RDF/XML serialized OWL for the Foundations ODM/OWL ontologies have been checked for syntactic errors and logical consistency with Protege 4 (http://protege.stanford.edu/), HermiT 1.3.7 (http://www.hermit-reasoner.com/) and Pellet 2.2 (http://clarkparsia.com/pellet/).
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
