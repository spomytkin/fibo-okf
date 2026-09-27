---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan product representations
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Representations about the loan product and the appropriateness of this for the borrower.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Covers responsible lending, consumer credit laws. See Aus Consumer Creti; US Reg Z and so on. In detail, this
      will include things like the representations about rates of interest, what people can or can''t say when offering a
      product to a customer. Reg Z: Promoting the informed use of consumer credit by .. implictions and cost Also right to
      cancel a lien on a consumer''s dwelling.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProduct
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/isAbout
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Representation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Representation
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/LoanProductRepresentations
sources:
- id: fibo-source-9d1d4cf0d4
  resource: references/fibo/LOAN/LoansGeneral/LoansRegulatory.rdf
  sha256: 9d1d4cf0d45e2966f6fbe27dd62486cdd11c427c2d40f7701ea8f1775769245b
  title: FIBO source LOAN/LoansGeneral/LoansRegulatory.rdf
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
title: loan product representations
type: Ontology Class
---

# loan product representations

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/LoanProductRepresentations>

## Definition

Representations about the loan product and the appropriateness of this for the borrower.

## Relationships

- **Subclass of**: [Representation](/concepts/fibo/FND/Agreements/Contracts/Representation.md)

## Constraints

- **[isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)**: some values from of type [LoanProduct](/concepts/fibo/LOAN/LoansSpecific/LoanProducts/LoanProduct.md)

## Annotations

- **label** (en): loan product representations
- **definition** (en): Representations about the loan product and the appropriateness of this for the borrower.
- **explanatoryNote** (en): Covers responsible lending, consumer credit laws. See Aus Consumer Creti; US Reg Z and so on. In detail, this will include things like the representations about rates of interest, what people can or can't say when offering a product to a customer. Reg Z: Promoting the informed use of consumer credit by .. implictions and cost Also right to cancel a lien on a consumer's dwelling.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
