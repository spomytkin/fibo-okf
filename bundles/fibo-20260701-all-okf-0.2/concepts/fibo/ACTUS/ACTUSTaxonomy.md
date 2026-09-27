---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology represents the ACTUS taxonomy as a controlled vocabulary and maps it to FIBO, providing the corresponding
      semantics and enabling integration of knowledge graphs based on FIBO with the ACTUS system.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2024-2026 ACTUS Financial Research Foundation\n2024-2026 EDM Association dba EDM Council, Inc.\n\
      Copyright (c) 2024-2025 Object Management Group, Inc.\n\nPermission is hereby granted, free of charge, to any person\
      \ obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without\
      \ restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,\
      \ and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the\
      \ following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or\
      \ substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\
      \ IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.\
      \ IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN\
      \ AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER\
      \ DEALINGS IN THE SOFTWARE.\n\t\t\nSee https://opensource.org/licenses/MIT."
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/source
    value: https://www.actusfrf.org
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS Controlled Vocabulary
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: This version of the ACTUS taxonomy, which is provisional in FIBO, is as of the end of June 2026. It is considered
      ACTUS 1.1 by the ACTUS team. We anticipate additional changes over the course of Q3 2026.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2024-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2024-2026 ACTUS Financial Research Foundation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2024-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy.md
    predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Provisional
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/TextDatatype/
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/
sources:
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: ACTUS Controlled Vocabulary
type: Ontology Definition
---

# ACTUS Controlled Vocabulary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [CodesAndCodeSets](<https://www.omg.org/spec/Commons/CodesAndCodeSets/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [TextDatatype](<https://www.omg.org/spec/Commons/TextDatatype/>)
- **Related to**: [ACTUSTaxonomy](/concepts/fibo/ACTUS/ACTUSTaxonomy.md)
- **Related to**: [Provisional](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md)

## Annotations

- **abstract**: This ontology represents the ACTUS taxonomy as a controlled vocabulary and maps it to FIBO, providing the corresponding semantics and enabling integration of knowledge graphs based on FIBO with the ACTUS system.
- **license**: Copyright (c) 2024-2026 ACTUS Financial Research Foundation 2024-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2024-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **source**: https://www.actusfrf.org
- **label**: ACTUS Controlled Vocabulary
- **note**: This version of the ACTUS taxonomy, which is provisional in FIBO, is as of the end of June 2026. It is considered ACTUS 1.1 by the ACTUS team. We anticipate additional changes over the course of Q3 2026.
- **copyright**: Copyright (c) 2024-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2024-2026 ACTUS Financial Research Foundation
- **copyright**: Copyright (c) 2024-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
