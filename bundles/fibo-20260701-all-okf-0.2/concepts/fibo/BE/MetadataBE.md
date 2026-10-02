---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: "This ontology provides metadata about the FIBO Business Entities (BE) Domain, which defines business concepts\
      \ for data governance, interoperability, and in regulatory reporting about business entities.\n\nThe scope of the BE\
      \ domain includes business and legal entity concepts that are considered by financial industry firms, regulators and\
      \ other industry participants relevant to financial services and more broadly, including:\n - Legal entities generally\n\
      \ - Corporate structure, ownership and control, including primary executive roles for businesses,\n - Functional entities\
      \ such as governments and government entities, non-governmental organizations, international organizations, not-for-profit\
      \ organizations, etc.\n - Concepts specific to corporations, partnerships, private limited companies, sole proprietorships,\
      \ and trusts."
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2018-08-27T18:00:00'
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2018-2026 Object Management Group\n\
      \nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation\
      \ files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use,\
      \ copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to\
      \ whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this\
      \ permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED\
      \ 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\nSee https://opensource.org/licenses/MIT."
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2026-04-15T18:00:00'
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Metadata about the FIBO Business Entities (BE) Domain
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/BE/MetadataBE.rdf version of this ontology was modified
      to eliminate informative Functional Entities ontologies, merging their content into others as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190401/MetadataBE.rdf version of the ontology and subordinate
      module-specific BE metadata ontologies were modified to use the Commons Ontology Library (Commons) Annotation Vocabulary
      rather than the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/MetadataBE.rdf version of the ontology was modified to
      merge details from the old corporations ontology into corporate bodies for consistency and useability (BE-259).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20251001/MetadataBE.rdf version of the ontology was modified to
      update metadata including providing an expanded domain name for usability in business glossaries (FND-404).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2018-2026 Object Management Group
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20260401/MetadataBE/
  - concept: /concepts/fibo/BE/FunctionalEntities/MetadataBEFunctionalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/MetadataBEFunctionalEntities/
  - concept: /concepts/fibo/BE/GovernmentEntities/MetadataBEGovernmentEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/MetadataBEGovernmentEntities/
  - concept: /concepts/fibo/BE/LegalEntities/MetadataBELegalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/MetadataBELegalEntities/
  - concept: /concepts/fibo/BE/OwnershipAndControl/MetadataBEOwnershipAndControl.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/MetadataBEOwnershipAndControl/
  - concept: /concepts/fibo/BE/Partnerships/MetadataBEPartnerships.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/MetadataBEPartnerships/
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/MetadataBEPrivateLimitedCompanies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/MetadataBEPrivateLimitedCompanies/
  - concept: /concepts/fibo/BE/SoleProprietorships/MetadataBESoleProprietorships.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/MetadataBESoleProprietorships/
  - concept: /concepts/fibo/BE/Trusts/MetadataBETrusts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/MetadataBETrusts/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/MetadataBE/
sources:
- id: fibo-source-6e5ef42b2f
  resource: references/fibo/BE/MetadataBE.rdf
  sha256: 6e5ef42b2f573f74c3d530fd09ae95616e55f5e47237ad6f500669fb258cab09
  title: FIBO source BE/MetadataBE.rdf
title: Metadata about the FIBO Business Entities (BE) Domain
type: Ontology Definition
---

# Metadata about the FIBO Business Entities (BE) Domain

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/MetadataBE/>

## Relationships

- **Related to**: [MetadataBEFunctionalEntities](/concepts/fibo/BE/FunctionalEntities/MetadataBEFunctionalEntities.md)
- **Related to**: [MetadataBEGovernmentEntities](/concepts/fibo/BE/GovernmentEntities/MetadataBEGovernmentEntities.md)
- **Related to**: [MetadataBELegalEntities](/concepts/fibo/BE/LegalEntities/MetadataBELegalEntities.md)
- **Related to**: [MetadataBEOwnershipAndControl](/concepts/fibo/BE/OwnershipAndControl/MetadataBEOwnershipAndControl.md)
- **Related to**: [MetadataBEPartnerships](/concepts/fibo/BE/Partnerships/MetadataBEPartnerships.md)
- **Related to**: [MetadataBEPrivateLimitedCompanies](/concepts/fibo/BE/PrivateLimitedCompanies/MetadataBEPrivateLimitedCompanies.md)
- **Related to**: [MetadataBESoleProprietorships](/concepts/fibo/BE/SoleProprietorships/MetadataBESoleProprietorships.md)
- **Related to**: [MetadataBETrusts](/concepts/fibo/BE/Trusts/MetadataBETrusts.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [MetadataBE](<https://spec.edmcouncil.org/fibo/ontology/BE/20260401/MetadataBE/>)

## Annotations

- **abstract**: This ontology provides metadata about the FIBO Business Entities (BE) Domain, which defines business concepts for data governance, interoperability, and in regulatory reporting about business entities.  The scope of the BE domain includes business and legal entity concepts that are considered by financial industry firms, regulators and other industry participants relevant to financial services and more broadly, including:  - Legal entities generally  - Corporate structure, ownership and control, including primary executive roles for businesses,  - Functional entities such as governments and government entities, non-governmental organizations, international organizations, not-for-profit organizations, etc.  - Concepts specific to corporations, partnerships, private limited companies, sole proprietorships, and trusts.
- **issued**: 2018-08-27T18:00:00
- **license**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2018-2026 Object Management Group  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **modified**: 2026-04-15T18:00:00
- **label**: Metadata about the FIBO Business Entities (BE) Domain
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/BE/MetadataBE.rdf version of this ontology was modified to eliminate informative Functional Entities ontologies, merging their content into others as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190401/MetadataBE.rdf version of the ontology and subordinate module-specific BE metadata ontologies were modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/MetadataBE.rdf version of the ontology was modified to merge details from the old corporations ontology into corporate bodies for consistency and useability (BE-259).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20251001/MetadataBE.rdf version of the ontology was modified to update metadata including providing an expanded domain name for usability in business glossaries (FND-404).
- **copyright**: Copyright (c) 2018-2026 EDM Association dba EDM Council, Inc.
- **copyright**: Copyright (c) 2018-2026 Object Management Group

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
