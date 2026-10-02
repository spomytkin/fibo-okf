---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines the concept of an agreement and roles that parties to an agreement play in the context of
      financial agreements. Agreements represent an understanding between parties, whereas contracts typically formalize such
      agreements.
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
    value: Agreements Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/Agreements/Agreements.owl version of the ontology was revised\
      \ in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n   (1) to use slash style URI/IRIss (also\
      \ called 303 URIs, vs. hash style) as required to support server side processing \n   (2) to use version-independent\
      \ IRIs for all definitions internally as opposed to version-specific IRIs\n   (3) to change the file suffix from .owl\
      \ to .rdf to increase usability in RDF tools\n   (4) to use 4-level abbreviations and corresponding namespace prefixes\
      \ for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n   (5) to incorporate changes\
      \ to the specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations.\n   (6) to revise a few of the definitions based on more formal sources."
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/Agreements/Agreement.rdf version of the ontology was
      modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Agreements/Agreement.rdf version of the ontology was
      modified per the issue resolutions identified in the FIBO FND 1.1 RTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.1/AboutFND-1.1/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Agreements/Agreement.rdf version of the ontology was
      modified per FIBO 2.0 RFC to add general concepts including obligor, obligee, and beneficiary in support of other FIBO
      domain areas.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Agreements/Agreement.rdf version of the ontology was
      modified to eliminate duplication of concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Agreements/Agreement.rdf version of the ontology was
      modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata
      vocabulary, clean up definitions to conform with ISO 704, add a missing restriction to mutual commitment, and eliminate
      an unnecessary reference to LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Agreements/Agreement.rdf version of the ontology was
      modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Agreements/Agreement.rdf version of the ontology was
      modified to add bilateral and multilateral agreement definitions (DER-55), and to eliminate certain constructs that
      are redundant and will never be materialized to reduce the number of nodes required for various contract-related searches,
      such as 'mutual agreement' (FND-391).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250501/Agreements/Agreement.rdf version of this ontology was
      modified to eliminate deprecated constructs that have been deprecated for more than a year (FND-407).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260601/Agreements/Agreements/
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
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/
sources:
- id: fibo-source-e7ad375c83
  resource: references/fibo/FND/Agreements/Agreements.rdf
  sha256: e7ad375c83c6ea909be45886e03aec3dd509a8c794a40149ee25f56176cbee08
  title: FIBO source FND/Agreements/Agreements.rdf
title: Agreements Ontology
type: Ontology Definition
---

# Agreements Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/>

## Relationships

- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [Agreements](<https://spec.edmcouncil.org/fibo/ontology/FND/20260601/Agreements/Agreements/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines the concept of an agreement and roles that parties to an agreement play in the context of financial agreements. Agreements represent an understanding between parties, whereas contracts typically formalize such agreements.
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Agreements Ontology
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/Agreements/Agreements.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:    (1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing     (2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs    (3) to change the file suffix from .owl to .rdf to increase usability in RDF tools    (4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure    (5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations.    (6) to revise a few of the definitions based on more formal sources.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/Agreements/Agreement.rdf version of the ontology was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Agreements/Agreement.rdf version of the ontology was modified per the issue resolutions identified in the FIBO FND 1.1 RTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.1/AboutFND-1.1/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Agreements/Agreement.rdf version of the ontology was modified per FIBO 2.0 RFC to add general concepts including obligor, obligee, and beneficiary in support of other FIBO domain areas.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Agreements/Agreement.rdf version of the ontology was modified to eliminate duplication of concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Agreements/Agreement.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary, clean up definitions to conform with ISO 704, add a missing restriction to mutual commitment, and eliminate an unnecessary reference to LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Agreements/Agreement.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Agreements/Agreement.rdf version of the ontology was modified to add bilateral and multilateral agreement definitions (DER-55), and to eliminate certain constructs that are redundant and will never be materialized to reduce the number of nodes required for various contract-related searches, such as 'mutual agreement' (FND-391).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250501/Agreements/Agreement.rdf version of this ontology was modified to eliminate deprecated constructs that have been deprecated for more than a year (FND-407).
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
