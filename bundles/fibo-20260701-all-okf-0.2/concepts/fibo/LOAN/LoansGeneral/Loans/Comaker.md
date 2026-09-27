---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: co-maker
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that signs a borrower's promissory note, providing additional security and potentially improving the quality
      of the debt
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Differences between a co-maker and co-borrower include: (1) a co-maker is not listed on the title of the asset
      to which the loan applies, (2) a co-maker does not have any legal ownership rights to the asset, and (3) the co-maker
      does not make regular payments on the loan unless the primary borrower(s) fails to do so.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The co-maker's liability is similar to that of an endorser or guarantor, but with additional risk/exposure, as
      they can be compelled to honor the debt much sooner and regardless of whether certain conditions are met.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: comaker
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: cosigner
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Comaker
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: co-maker
type: Ontology Class
---

# co-maker

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Comaker>

## Definition

party that signs a borrower's promissory note, providing additional security and potentially improving the quality of the debt

## Relationships

- **Subclass of**: [ContractThirdParty](/concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md)

## Annotations

- **label**: co-maker
- **definition**: party that signs a borrower's promissory note, providing additional security and potentially improving the quality of the debt
- **explanatoryNote**: Differences between a co-maker and co-borrower include: (1) a co-maker is not listed on the title of the asset to which the loan applies, (2) a co-maker does not have any legal ownership rights to the asset, and (3) the co-maker does not make regular payments on the loan unless the primary borrower(s) fails to do so.
- **explanatoryNote**: The co-maker's liability is similar to that of an endorser or guarantor, but with additional risk/exposure, as they can be compelled to honor the debt much sooner and regardless of whether certain conditions are met.
- **synonym**: comaker
- **synonym**: cosigner

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
